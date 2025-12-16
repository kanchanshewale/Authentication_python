from flask import Blueprint, jsonify
from db import get_connection
from utils.decorators import token_required, admin_required

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["GET"])
@token_required
@admin_required
def get_users():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id,name,email,role FROM users")
    users = cur.fetchall()
    conn.close()
    return jsonify(users)


@user_bp.route("/users/<int:id>", methods=["DELETE"])
@token_required
@admin_required
def delete_user(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"})
