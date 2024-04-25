
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def secure_file_name(file_name):
    return secure_filename(file_name)