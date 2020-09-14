import base64
import datetime
from flask import Blueprint, request, make_response, jsonify, url_for
from project import app, socketio
from project.helpers import ocr_space_file

bp = Blueprint('api', __name__)


@bp.route('/test/upload', methods=['GET'])
def test():
    """
    Test ESP32 Upload
    """
    sn = ""
    try:
        post_data = request.get_json()

        sn = request.values.get('device', "")  # post_data.get('device', "")
        sampling = post_data.get('sampling', "")
        if not sampling:
            sampling = datetime.datetime.utcnow()
        print(sampling)

        imageStr = post_data.get('image')
        if imageStr:
            file_name = f"test-{sn}.jpg"
            img_file = f"{app.config['UPLOAD_FOLDER']}{file_name}"
            # print(file_name)
            # img_file = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

            imgdata = base64.b64decode(imageStr)
            with open(img_file, 'wb') as f:
                f.write(imgdata)

            ocr_scanning = ocr_space_file(filename=img_file, api_key=app.config['OCR_SPACE_API_KEY'])
            # print(ocr_scanning['ParsedResults'][0]['ParsedText'])

            print("saving image !")
            result = {
                "status": "success",
                "message": "Upload Succeed",
                "data": {
                    "serial_number": sn,
                    "sampling": sampling,
                    "image_url": img_file,
                    "result": ocr_scanning['ParsedResults'][0]['ParsedText']
                }
            }
        else:
            result = {
                "status": "failed",
                "message": "Device sends empty image string",
                "data": {
                    "serial_number": sn,
                    "sampling": sampling,
                    "image_url": url_for('static', filename="images/placeholder.jpg"),
                    "result": None
                }
            }
    except Exception as e:
        result = {
            "status": "error",
            "message": f"Error : {e}",
            "data": {
                "image_url": url_for('static', filename="images/placeholder.jpg"),
                "result": None,
                "sampling": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            }
        }
    if sn:
        print("Sending message through socket io!")
        socketio.emit(f"status-{sn}", result, namespace='/test', broadcast=True)

    return make_response(jsonify(result)), 200
