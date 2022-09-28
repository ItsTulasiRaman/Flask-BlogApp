To create db file (mandatory):
    1. >>> from app import db
    2. >>> db.create_all()  -> creates the .db file configured in app 

To test BlogPost database in terminal:
    1.Change directory to the app.py and posts.db present folder.

In the terminal:
    1. >>> from app import db
    2. >>> from app import BlogPost -> importing db from app
    3. >>> BlogPost.query.all()
        []                           -> This outputs because we have not inserted any data yet
    4. >>> db.session.add(BlogPost(title='Blog Post 1',content='This is a content of Blog Post 1',author='Gennie'))            ->Data is inserted
    5. >>> db.session.add(BlogPost(title='Blog Post 2',content='This is a content of Blog Post 2',author='Jenny'))
    6. >>> BlogPost.query.all()
        [Blog post 1, Blog post 2]     -> Outputs and creates a new file as posts.db-journal

Fetching db data:
    7. >>> BlogPost.query.all()[0].id
        1
    8. >>> BlogPost.query.all()[0].content
        'This is a content of Blog Post 1'
    9. >>> BlogPost.query.all()[1].id
        2
    10. >>> BlogPost.query.all()[0].author
        'Gennie'
    11. >>> BlogPost.query.all()[0].date_posted
        datetime.datetime(2022, 7, 29, 21, 7, 36, 359883)
    12. >>> BlogPost.query.all()[1].content
        'This is a content of Blog Post 2'
    13. >>> BlogPost.query.all()[1].author
        'Jenny'
    14. >>> BlogPost.query.all()[1].date_posted
        datetime.datetime(2022, 7, 29, 21, 7, 36, 362441)
    15. >>> BlogPost.query[1]             //BlogPost.query[index element] supports in sqlalchemy
        Blog post 2
    16.>>> BlogPost.query.filter_by(title='Second BlogPost via web')
        <flask_sqlalchemy.BaseQuery object at 0x7f7fe597b190>
    17.>>> BlogPost.query.filter_by(title='Second BlogPost via web').all()
        [Blog post 2]
(Important: get() only requires the primary key id to fetch the BlogPost object)
    18.>>> BlogPost.query.get(1)
        Blog post 1
    19.>>> BlogPost.query.get(0)         //displays nothing as there is no BlogPost 0
    20.>>> BlogPost.query.get(2)
        Blog post 2
To delete in flask_sqlalchemy:
    21.>>> db.session.delete(BlogPost.query.get(2))
       >>> BlogPost.query.all()
    [Blog post 1, Blog post 3]
    22.>>> BlogPost.query.get(1).author
        'Anonymous'
       >>> BlogPost.query.get(1).author = 'Francis'
       >>> BlogPost.query.get(1).author
        'Francis'
(Note: Use db.session.commit() to see the changes in the website. Using these commands in terminal only makes changes 
temporarily(i.e unsaved if you disconnect your localhost/shutdown vs code or PC.).)
