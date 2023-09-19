from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'view is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]


def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a><h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')


def create(request):
    article = '''
    <form action="/create/">
        <p><input type="text" name ="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body></textarea></p>
        <p><input type="submit"></p>
        '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    return HttpResponse('Read!'+id)