import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown


POSTS = {}

for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)

    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])

    
POSTS = {
    post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}

env = Environment(loader=PackageLoader('main', 'templates'))
home_template = env.get_template('home.html')
post_template = env.get_template('post.html')

posts_metadata = [POSTS[post].metadata for post in POSTS]
tags = [post['tags'] for post in posts_metadata]
home_html = home_template.render(posts=posts_metadata, tags=tags)

with open('../mydemo/index.html', 'w') as file:
    file.write(home_html)

for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date']
    }

    post_html = post_template.render(post=post_data)
    post_file_path = '../mydemo/posts/{slug}.html'.format(slug=post_metadata['slug'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)


"""
import os 
from datetime import datetime
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

POSTS = {}

for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)

    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])
POSTS = {
    post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}

env = Environment(loader=PackageLoader('main', 'templates'))
home_template = env.get_template('home.html')
post_template = env.get_template('post.html')

posts_metadata = [POSTS[post].metadata for post in POSTS]
home_html = home_template.render(posts=posts_metadata)

posts_metadata = [POSTS[post].metadata for post in POSTS]
tags = [post['tags'] for post in posts_metadata]



home_html = home_template.render(posts=posts_metadata, tags=tags)

os.make
with open('../recipes/home.html', 'w') as file:
    file.write(home_html)

for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date'],
    }

    post_html = post_template.render(post=post_data)

    post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html)
"""
'''
with open('content/turkish-pide.md', 'r') as file:
    parsed_md = markdown(file.read(), extras=['metadata'])

    env = Environment(loader=PackageLoader('main', 'templates'))
    test_template = env.get_template('test.html')

    data = {
    'content': parsed_md,
    'title': parsed_md.metadata['title'],
    'date': parsed_md.metadata['date']
    }

    print(test_template.render(post=data))
'''