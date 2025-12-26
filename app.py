from flask import Flask, render_template
from flask_cors import CORS
from database import db, init_db, get_db
from config import Config

# Импорт всех routes
from routes.products import products_bp
from routes.workshops import workshops_bp
from routes.material import material_bp
from routes.product_types import product_types_bp
from routes.product_workshops import product_workshops_bp
from routes.material_types import material_types_bp

app = Flask(__name__, template_folder='static', static_folder='static')
app.config.from_object(Config)

# ✅ Инициализировать БД (ВСЕ в database.py!)
init_db(app)

CORS(app)

# Регистрация всех blueprints
app.register_blueprint(products_bp)
app.register_blueprint(workshops_bp)
app.register_blueprint(material_bp)
app.register_blueprint(product_types_bp)           # НОВАЯ
app.register_blueprint(material_types_bp)          # НОВАЯ
app.register_blueprint(product_workshops_bp)       # НОВАЯ

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')

@app.teardown_appcontext
def close_connection(exception):
    """Закрытие подключения БД"""
    db_session = getattr(app, '_database', None)
    if db_session is not None:
        db_session.close()

if __name__ == '__main__':
    with app.app_context():
        print("🚀 Приложение запущено!")
        print("📱 Перейди по адресу: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
