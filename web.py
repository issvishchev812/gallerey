from flask import Flask, url_for, request, redirect, render_template_string
import os

app = Flask(__name__)

arr = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

planets_info = {
    'Меркурий': ['Ближайшая планета к Солнцу.', 'Самая маленькая планета в Солнечной системе.',
                 'Поверхность покрыта кратерами, похожими на лунные.',
                 'Нет атмосферы, поэтому температура сильно колеблется: от −180 °C до +430 °C.'],
    'Венера': ['Вторая планета от Солнца.',
               'Обладает самой плотной атмосферой среди планет земной группы, состоящей в основном из углекислого газа.',
               'Температура поверхности достигает около 460 °C, что делает её самой горячей планетой.',
               'Вращается вокруг своей оси в обратном направлении (ретроградное вращение).'],
    'Земля': ['Третья планета от Солнца.', 'Единственная известная планета с жизнью.',
              'Атмосфера состоит преимущественно из азота и кислорода.',
              'Покрыта на 71% водой, что делает её уникальной среди планет земной группы.'],
    'Марс': ['Четвёртая планета от Солнца.', 'Известна своими полярными ледяными шапками, содержащими воду.',
             'Красный цвет планеты обусловлен высоким содержанием оксида железа (ржавчины) в почве.',
             'На Марсе находятся самые высокие горы в Солнечной системе, включая вулкан Олимп.'],
    'Юпитер': ['Пятая планета от Солнца.', 'Самая большая планета в Солнечной системе.',
               'Имеет сильное магнитное поле, которое защищает её спутники от солнечного ветра.',
               'Известен своим Большим красным пятном — гигантским штормом, который существует уже сотни лет.'],
    'Сатурн': ['Шестая планета от Солнца.', 'Знаменита своими яркими кольцами, состоящими из льда, пыли и камней.',
               'Обладает множеством спутников, самый известный из которых — Титан, имеющий плотную атмосферу.',
               'Плотность Сатурна настолько мала, что он мог бы плавать в воде, если бы существовал достаточно большой океан.'],
    'Уран': ['Седьмая планета от Солнца.',
             'Уникальна тем, что лежит практически на боку — ось вращения наклонена почти параллельно плоскости орбиты.',
             'Холодная планета с температурой около −224 °C.', 'Имеет кольца, хотя они менее заметны, чем у Сатурна.'],
    'Нептун': ['Восьмая и самая далёкая планета от Солнца.',
               'Обладает мощными ветрами, скорость которых превышает 2000 км/ч.',
               'Голубой цвет планеты обусловлен наличием метана в атмосфере.',
               'Самый крупный спутник Нептуна — Тритон, имеет ретроградную орбиту и гейзеры.']
}


@app.route('/')
def a():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def pr():
    return '</br>'.join(arr)


@app.route('/image_mars')
def m():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/OSIRIS_Mars_true_color.jpg')}" 
                        <p></br>вот она какая красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/OSIRIS_Mars_true_color.jpg')}">
                    <div class="alert alert-dark" role="alert">
                        {arr[0]}
                    </div>
                    <div class="alert alert-success" role="alert">
                        {arr[1]}
                    </div>
                    <div class="alert alert-info" role="alert">
                        {arr[2]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                        {arr[3]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                        {arr[4]}
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендентa</h1> .
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="know">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <label for="classSelect">Какие у вас профессии</label>
                                     <div class="form-group form-check">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                        <label class="form-check-label" for="a">пилот</label>
                                        <input type="checkbox" class="form-check-input" id="a" name="accept">
                                    </div>
                                     <div class="form-group form-check">
                                        <label class="form-check-label" for="aa">строитель</label>
                                        <input type="checkbox" class="form-check-input" id="aa" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                        <label class="form-check-label" for="aaa">экзобиолог</label>
                                        <input type="checkbox" class="form-check-input" id="aaa" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                        <label class="form-check-label" for="aaaa">врач</label>
                                        <input type="checkbox" class="form-check-input" id="aaaa" name="accept">
                                    </div>    
                                    <div class="form-group form-check">
                                        <label class="form-check-label" for="b">инженер по терраформированию,</label>
                                        <input type="checkbox" class="form-check-input" id="b" name="accept">
                                    </div>                   
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['know'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"



@app.route('/choice/<planet_name>')
def planet(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-dark" role="alert">
                            {planets_info[planet_name][0]}
                        </div>
                        <div class="alert alert-success" role="alert">
                            {planets_info[planet_name][1]}
                        </div>
                        <div class="alert alert-info" role="alert">
                            {planets_info[planet_name][2]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                            {planets_info[planet_name][3]}
                        </div>
                      </body>
                    </html>'''



@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие в миссии {nickname}:</h2>
                            <div class="alert alert-dark" role="alert">
                                Поздравляем! Ваш рейтинг после {level} этапа отбора
                            </div>
                            <div class="alert alert-success" role="alert">
                                составляет {rating}!
                            </div>
                            <div class="alert alert-info" role="alert">
                                Желаем удачи
                            </div>
                          </body>
                        </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file" required>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

    elif request.method == 'POST':
        file = request.files['file']
        if file and file.filename:  # убедимся, что файл загружен и имеет имя
            filepath = os.path.join('static', 'img', file.filename)
            file.save(filepath)
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h2 align="center">для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file" required>
                                        </div>
                                        <img src="{url_for('static', filename='img/' + file.filename)}" class="img-fluid mt-3" alt="Загруженная фотография" />
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''

    return redirect(url_for('load_photo'))



images = [
    'static/img/pm1.jpg',
    'static/img/pm2.jpg',
    'static/img/pm3.jpg'
]


@app.route('/carousel')
def gallery():
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Галерея марсианских ландшафтов</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="text-center">Галерея марсианских ландшафтов</h1>
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <div class="carousel-inner">
                    {% for image in images %}
                    <div class="carousel-item {% if loop.index == 1 %}active{% endif %}">
                        <img src="{{ image }}" class="d-block w-100" alt="Марсианский ландшафт">
                    </div>
                    {% endfor %}
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    '''

    return render_template_string(template, images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')







