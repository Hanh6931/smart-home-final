from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import json
import platform  
import subprocess
import numpy as np
import random
import time
import mysql.connector
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from joblib import dump, load
from threading import Thread
from datetime import datetime

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.secret_key = secrets.token_hex(16)
threads_started = False  # 用于线程状态管理
# Remote database connection settings
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="wayne.cs.uwec.edu",  # Remote server hostname
            user="XUL3227",           # Username
            password="4C1LW181",      # Password
            database="cs485group4",   # Database name
            port=3306,                # Default MySQL port
            connection_timeout=10     # Set connection timeout
        )
        if connection.is_connected():
            print("Successfully connected to remote database: cs485group4")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# SQLAlchemy integration for Flask with remote database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://XUL3227:4C1LW181@wayne.cs.uwec.edu:3306/cs485group4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Test the remote connection
if connect_to_database():
    print("Remote database connection is successful!")
else:
    print("Failed to connect to the remote database.")


class Bathroom(db.Model):
    __tablename__ = 'bathroom'
    room_id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, nullable=False)

class Bedroom(db.Model):
    __tablename__ = 'bedroom'
    room_id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, nullable=False)

class Device(db.Model):
    __tablename__ = 'device'
    device_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer)
    device_type_id = db.Column(db.Integer)
    status = db.Column(db.String(10), nullable=False, default='Off')
    brightness = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    position = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    setting = db.Column(db.JSON)
    user_id = db.Column(db.Integer)

    def to_json(self):
        json_data = json.dumps({
            "device_id": self.device_id,
            "room_id": self.room_id,
            "device_type_id": self.device_type_id,
            "status": self.status,
            "brightness": self.brightness,
            "temperature": self.temperature,
            "position": self.position,
            "updated_at": str(self.updated_at),
            "setting": self.setting
        })
        return json_data



class DeviceLogs(db.Model):
    __tablename__ = 'device_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    device_id = db.Column(db.Integer)
    action_taken = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class DeviceType(db.Model):
    __tablename__ = 'device_type'
    device_type_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), nullable=False)

class Home(db.Model):
    __tablename__ = 'home'
    home_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer)

class Kitchen(db.Model):
    __tablename__ = 'kitchen'
    room_id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, nullable=False)

class LivingRoom(db.Model):
    __tablename__ = 'living_room'
    room_id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, nullable=False)

class Rooms(db.Model):
    __tablename__ = 'rooms'
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer)

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    home_address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    family_members = db.Column(db.Integer, nullable=False)
    reset_token = db.Column(db.String(255))
    reset_expires = db.Column(db.DateTime)
##########
class UserLocation(db.Model):
    __tablename__ = 'user_location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)  # 默认使用当前时间
    room = db.Column(db.Integer, nullable=True)


# 2. 随机数据插入 wifi_signals 表
def insert_random_data_to_wifi_signals():
    """每隔 5 秒插入随机 Wi-Fi 信号数据到 wifi_signals 表"""
    while True:
        connection = connect_to_database()
        if not connection:
            print("Failed to connect to database for data insertion.")
            time.sleep(5)
            continue

        try:
            random_data = [random.randint(-90, -30) for _ in range(7)]  # 模拟 Wi-Fi 信号强度
            cursor = connection.cursor()
            query = """
            INSERT INTO random_wifi_signals (signal_1, signal_2, signal_3, signal_4, signal_5, signal_6, signal_7)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, tuple(random_data))
            connection.commit()
            print(f"Inserted into wifi_signals: {random_data}")
        except mysql.connector.Error as e:
            print(f"Error inserting random data: {e}")
        finally:
            connection.close()  # 确保关闭连接
        time.sleep(5)

# 3. 从 random_wifi_signals 表获取最新数据
def fetch_latest_random_wifi_signals():
    """从 random_wifi_signals 表获取最新数据"""
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to database for fetching data.")
        return None

    try:
        cursor = connection.cursor()
        query = """
        SELECT signal_1, signal_2, signal_3, signal_4, signal_5, signal_6, signal_7
        FROM random_wifi_signals ORDER BY id DESC LIMIT 1
        """
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print(f"Fetched from random_wifi_signals: {result}")
            return np.array(result).reshape(1, -1)
        else:
            print("No data in random_wifi_signals.")
            return None
    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        connection.close()  # 确保关闭连接

# 4. 预测所在房间并插入 user_location 表
def predict_and_insert_user_location(svm_wifi_model, scaler):
    """基于 random_wifi_signals 数据预测房间并插入到 user_location"""
    while True:
        connection = connect_to_database()
        if not connection:
            print("Failed to connect to database for prediction.")
            time.sleep(5)
            continue

        try:
            wifi_signals = fetch_latest_random_wifi_signals()
            if wifi_signals is None:
                time.sleep(5)
                continue

            # 标准化数据并预测房间
            wifi_signals_scaled = scaler.transform(wifi_signals)
            predicted_room = int(svm_wifi_model.predict(wifi_signals_scaled)[0])
            print(f"Predicted room: {predicted_room}")

            # 插入预测结果到 user_location
            cursor = connection.cursor()
            query = "INSERT INTO user_location (room, timestamp) VALUES (%s, NOW())"
            cursor.execute(query, (predicted_room,))
            connection.commit()
            print(f"Inserted into user_location: room={predicted_room}")
        except mysql.connector.Error as e:
            print(f"Error inserting user location: {e}")
        except Exception as e:
            print(f"Prediction error: {e}")
        finally:
            connection.close()  # 确保关闭连接
        time.sleep(5)

# 5. 加载或训练模型
def load_or_train_model():
    """加载模型或训练新模型"""
    try:
        svm_wifi_model = load('svm_wifi_localization_model.joblib')
        scaler = load('scaler.joblib')
        print("Models loaded successfully.")
    except FileNotFoundError:
        print("Model files not found. Please train a new model.")
        exit()  # 如果模型不存在，则直接退出程序
    return svm_wifi_model, scaler


def login_required(func):
    def wrapper(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            # 未登录时可以重定向到登录页面或返回错误信息
            return render_template('smarthome/index.html')
        return func(*args, **kwargs)
    return wrapper

@app.route('/login',methods=['GET','POST'], endpoint="login")
def login():
    global threads_started

    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = Users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.user_id
            session['username'] = user.username
            session['logged_in'] = True
            # 在用户登录成功后启动 WiFi 服务
            if not threads_started:
                threads_started = True
                print("Starting WiFi location service...")

                # 加载模型
                svm_wifi_model, scaler = load_or_train_model()

                # 启动线程
                thread_insert = Thread(target=insert_random_data_to_wifi_signals, daemon=True)
                thread_predict = Thread(target=predict_and_insert_user_location, args=(svm_wifi_model, scaler),
                                        daemon=True)

                thread_insert.start()
                thread_predict.start()

                print("WiFi location service is running in the background.")
            return jsonify({'success': True, 'redirect_url': '/'})
        else:
            return jsonify({'success': False})
    else:
        return render_template("smarthome/index.html")


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/register',methods=['GET','POST'],endpoint="register")
def register():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            data['password'] = generate_password_hash(data['password'])
            data.pop('confirm-password')
            new_user = Users(**data)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'success': True, 'redirect_url': '/login'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    else:
        return render_template("smarthome/signup.html")


@app.route('/forgot_password',methods=['GET','POST'], endpoint="forgot_password")
def forgot_password():
    if request.method == 'POST':
        try:
            username = request.form['username']
            old_password = request.form['old-password']
            new_password = request.form['new-password']

            user = Users.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, old_password):
               user.password = generate_password_hash(new_password)
               db.session.commit()
               return jsonify({'success': True, 'redirect_url': '/login'})
            else:
                return jsonify({'success': False, 'error': 'User not found or password incorrect'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    else:
        return render_template("smarthome/forgot-password.html")

def inint_device(room_id,device_type,user_id):
    device = Device.query.filter_by(room_id=room_id, device_type_id=device_type, user_id=user_id).first()
    print(device)
    if device is None:
        if device_type == 1:
            # light
            device = Device(
                            user_id=user_id,room_id=room_id, device_type_id='1',
                           brightness=0, setting=json.dumps({"RGB": [0, 0, 0]}))
        elif device_type == 2:
            # curtain
            device = Device(user_id=user_id,room_id=room_id, device_type_id='2',
                             setting=json.dumps({"curtain": [50, 50]}))
        elif device_type == 3:
            # ac
            device = Device(user_id=user_id,room_id=room_id, device_type_id='3',
                            setting=json.dumps({"mode": "Cool"}))
        elif device_type == 4:
            # range_hood
            device = Device(user_id=user_id,room_id=room_id, device_type_id='4',
                            setting=json.dumps({"Fan_speed": 0}))
        db.session.add(device)
        db.session.commit()
    return device



@app.route('/bedroom', methods=['GET','POST'],endpoint='bedroom_route')
@login_required
def bedroom():
    username = session["username"]
    latest_room = UserLocation.query.order_by(UserLocation.timestamp.desc()).first()
    # 确保 latest_room 不为 None，防止数据库为空导致报错
    current_room = latest_room.room if latest_room else None
    return render_template("smarthome/bedroom.html",**locals())


@app.route('/',methods=['GET', 'POST'],endpoint='home')
@login_required
def floor_plan():
    latest_room = UserLocation.query.order_by(UserLocation.timestamp.desc()).first()

    # 确保 latest_room 不为 None，防止数据库为空导致报错
    current_room = latest_room.room if latest_room else None
    username = session["username"]
    return render_template("smarthome/floorplan.html",username=username, current_room=current_room)





@app.route("/start_wifi_service", methods=["GET"])
def start_wifi_location_service():
    # 加载模型
    svm_wifi_model, scaler = load_or_train_model()

    # 启动线程进行数据插入和预测
    try:
        from threading import Thread
        thread_insert = Thread(target=insert_random_data_to_wifi_signals)
        thread_predict = Thread(target=predict_and_insert_user_location, args=(svm_wifi_model, scaler))

        thread_insert.start()
        thread_predict.start()

        thread_insert.join()
        thread_predict.join()
    except KeyboardInterrupt:
        print("Program terminated by user.")

@app.route('/kitchen',methods=['GET','POST'],endpoint='kitchen')
@login_required
def kitchen():
    username = session["username"]
    latest_room = UserLocation.query.order_by(UserLocation.timestamp.desc()).first()

    # 确保 latest_room 不为 None，防止数据库为空导致报错
    current_room = latest_room.room if latest_room else None
    return render_template("smarthome/kitchen.html",**locals())


@app.route('/living_room',methods=['GET','POST'], endpoint='living_room')
@login_required
def living_room():
    username = session["username"]
    latest_room = UserLocation.query.order_by(UserLocation.timestamp.desc()).first()

    # 确保 latest_room 不为 None，防止数据库为空导致报错
    current_room = latest_room.room if latest_room else None
    return render_template("smarthome/living-room.html",**locals())


@app.route('/bathroom', methods=['GET', 'POST'], endpoint='bathroom_route')
@login_required
def bathroom():
    username = session["username"]
    latest_room = UserLocation.query.order_by(UserLocation.timestamp.desc()).first()

    # 确保 latest_room 不为 None，防止数据库为空导致报错
    current_room = latest_room.room if latest_room else None
    return render_template("smarthome/bathroom.html",**locals())


@app.route('/get_device',methods=['GET', 'POST'],endpoint='get_device')
@login_required
def get_device():
    # try:
    data = request.get_json()
    user_id = session['user_id']
    room_id = data['room_id']
    device_type_id = data['device_type_id']
    device = inint_device(room_id, device_type_id,user_id).to_json()
    return jsonify({'success': True, 'device': device})
    # except Exception as e:
    #     return jsonify({'success': False, 'error': str(e)})

@app.route('/set_device',methods=['GET', 'POST'], endpoint='set_device')
@login_required
def set_device():
    try:
        data = request.get_json()
        user_id = session["user_id"]
        room_id = data['room_id']
        device_type_id = data['device_type_id']
        device = Device.query.filter_by(room_id=room_id, user_id=user_id, device_type_id=device_type_id).first()
        new_setting = data['data']
        new_setting["setting"] = json.dumps(new_setting["setting"])
        for key, value in new_setting.items():
            setattr(device, key, value)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/start_voice_recognition', methods=['POST'])
def start_voice_recognition():
    """
    通过语音命令更新数据库设备状态
    """
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for command...")
            audio = recognizer.listen(source)

        # 识别语音命令
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")

        # 分析命令并更新数据库
        if command == "turn on light bedroom":
            update_device_status(1, 1, "On")  # 假设灯的 device_type_id 是 1，room_id 是 1
        elif command == "turn off light bedroom":
            update_device_status(1, 1, "Off")
        else:
            return jsonify({"success": False, "error": "Unknown command"})

        return jsonify({"success": True, "command": command})
    except sr.UnknownValueError:
        return jsonify({"success": False, "error": "Could not understand the audio"})
    except sr.RequestError as e:
        return jsonify({"success": False, "error": str(e)})

def update_device_status(device_type_id, room_id, status):
    """
    更新设备状态到数据库
    """
    try:
        device = Device.query.filter_by(room_id=room_id, device_type_id=device_type_id).first()
        if device:
            device.status = status
            db.session.commit()
            print(f"Updated device {device_type_id} in room {room_id} to {status}")
        else:
            print(f"No device found for type {device_type_id} in room {room_id}")
    except Exception as e:
        print(f"Error updating device status: {e}")



if __name__ == '__main__':
    app.run(debug=True)
