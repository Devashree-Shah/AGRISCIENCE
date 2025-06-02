from flask import Flask
from routes.crop_routes import crop_bp
from routes.field_routes import field_bp
from routes.weather_routes import weather_bp

app = Flask(_name_)

# Register Blueprints
app.register_blueprint(crop_bp)
app.register_blueprint(field_bp)
app.register_blueprint(weather_bp)

if _name_ == "_main_":
    app.run(debug=True)
