from flask import Blueprint, jsonify
from flask import request, redirect, abort, jsonify
from .models import Link
from .database import db
from nanoid import generate

bp = Blueprint('links', __name__)

@bp.route('/links', methods=['GET'])
def get_links():
  """
  Retorna a lista de links encurtados
  ---
  tags:
    - Links
  responses:
    200:
      description: Lista de links
      schema:
        type: object
        properties:
          links:
            type: array
            items:
              type: object
              properties:
                id:
                  type: integer
                original_url:
                  type: string
                short_url:
                  type: string
  """

  base_url = request.host_url.rstrip('/')
  links = Link.query.all()
  result = [{"id": link.id, "original_url": link.original_url, "short_url": f"{base_url}/{link.short_id}"} for link in links]

  return jsonify({"links": result})

@bp.route("/link/create", methods=['POST'])
def create_link():
  """
  Cria um novo link encurtado
  ---
  tags:
    - Links
  parameters:
    - in: body
      name: body
      required: true
      schema:
        type: object
        properties:
          original_url:
            type: string
            description: URL original a ser encurtada
            example: "https://www.example.com"
  responses:
    201:
      description: Mensagem de sucesso
      schema:
        type: object
        properties:
          message:
            type: string
    400:
      description: Mensagem de erro
      schema:
        type: object
        properties:
          message:
            type: string
  """

  data = request.get_json()
  original_url = data.get("original_url")

  if not original_url:
    return jsonify({"message": "Original URL is required"}), 400
  
  short_id = generate(size=10)

  new_link = Link(original_url=original_url, short_id=short_id)
  db.session.add(new_link)
  db.session.commit()

  return jsonify({ "message": "Link created successfully" }), 201

@bp.route("/<short_id>", methods=['GET'])
def get_link(short_id):
  link = Link.query.filter_by(short_id=short_id).first()

  if not link:
    abort(404)
  else:
    return redirect(link.original_url)

@bp.route("/link/<int:link_id>", methods=['DELETE'])
def delete_link(link_id):
  """
  Deleta um link encurtado
  ---
  tags:
    - Links
  parameters:
    - in: path
      name: link_id
      required: true
      type: integer
      description: ID do link a ser deletado
  responses:
    200:
      description: Link deletado com sucesso
      schema:
        type: object
        properties:
          message:
            type: string
    404:
      description: Link não encontrado
      schema:
        type: object
        properties:
          message:
            type: string
  """
  
  link = Link.query.get(link_id)
  
  if not link:
    return jsonify({"message": "Link not found"}), 404
  
  db.session.delete(link)
  db.session.commit()
  
  return jsonify({"message": "Link deleted successfully"}), 200