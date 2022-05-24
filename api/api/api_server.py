from datetime import datetime, timedelta
from flask import jsonify, request

from . import api
from .errors import bad_request
from .. import db
from ..models import WeathModel


@api.route("/", methods=["GET"])
def get_list():
    try:
        # validators data
        if "radius" in request.args and "lat" in request.args and "lng" in request.args:
            # radius
            radius = float(request.args.get("radius"))
            if radius > 500 or radius < 0:
                return bad_request("radius does not fit")
            # latitude
            lat = float(request.args.get("lat"))
            if lat > 90.0 or lat < -90.0:
                return bad_request("lat does not fit")
            # longitude
            lng = float(request.args.get("lng"))
            if lng > 180.0 or lat < -180.0:
                return bad_request("lng does not fit")
            # getting data
            datas = db.engine.execute(
                f"""
                    SELECT latitude,longitude,temperature,timess, (6371 * acos(cos(radians({lat}))
                        * cos(radians(latitude)) * 
                        cos(radians(longitude) - radians({lng})) + sin(radians({lat})) * 
                        sin( radians(latitude)))) AS distance FROM weathers 
                    WHERE (3959 * acos(cos(radians({lat})) * cos(radians(latitude)) * 
                        cos(radians(longitude) - radians({lng})) + sin(radians({lat})) * 
                        sin(radians(latitude)))) < {radius} 
                    ORDER BY distance;"""
            ).fetchall()
            # json
            json_datas_page = [
                {
                    "lat": i.latitude,
                    "lng": i.longitude,
                    "temperature": i.temperature,
                    "time": i.timess.strftime("%Y-%m-%d %H:%M:%S"),
                }
                for i in datas
            ]

            return jsonify(json_datas_page)
        else:
            return bad_request("not args")
    except ValueError:
        return bad_request("Value error")


@api.route("/", methods=["POST"])
def post_list():
    request_data = request.get_json()
    try:
        # validators data
        date = datetime.strptime(request_data["time"], "%Y-%m-%d %H:%M:%S")
        if date > (datetime.now() + timedelta(minutes=1)) or date < (
            datetime.now() - timedelta(days=2)
        ):
            return bad_request("date invalid")
        if (
            -90.00 < float(request_data["lat"]) < 90.00
            and -180.00 < float(request_data["lng"]) < 180.00
        ):
            if request_data["temperature"]:
                # writing a new record
                weather = WeathModel(
                    latitude=float(request_data["lat"]),
                    longitude=float(request_data["lng"]),
                    temperature=int(request_data["temperature"]),
                    timess=date,
                    date_del=date + timedelta(days=2),
                )
                db.session.add(weather)
                db.session.commit()
                return ""
            else:
                return bad_request("temperature none")
        else:
            return bad_request("lon or lat invalid")
    except:
        return bad_request("there is no data")