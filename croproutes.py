from flask import Blueprint, jsonify
from models.db import get_db_connection

crop_bp = Blueprint('crop_bp', _name_)

@crop_bp.route('/api/crops', methods=['GET'])
def get_crops():
    conn = get_db_connection()
    crops = conn.execute('SELECT * FROM crops').fetchall()
    conn.close()
    return jsonify([dict(row) for row in crops])
