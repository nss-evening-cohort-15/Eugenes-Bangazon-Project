import sqlite3
from django.shortcuts import render
from bangazon_api.models import Store
from bangazon_reports.views import Connection

def favstore_list(request):
  if request.method == 'GET':
    with sqlite3.connect(Connection.db_path) as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
        SELECT
          s.id,
          s.name,
          u.id user_id,
          u.first_name
        FROM
          bangazon_api_store s
        JOIN
          bangazon_api_favorite f ON f.store_id = s.id
        JOIN
          auth_user u on f.customer_id = u.id
      """)
      dataset = db_cursor.fetchall()
      
      favstore_by_user = {}
      
      for row in dataset:
        user_name = row['first_name']
        user_id = row['user_id']
        store_name = row['name']
        # store = Store()
        # store.name = row["name"]
        # uid = row["user_id"]
        if user_id in favstore_by_user:
          favstore_by_user[user_id]['stores'].append(store_name)
        else:
          favstore_by_user[user_id] = {
            'name': user_name,
            'stores': [store_name]
          }
    list_of_users_with_favs = favstore_by_user.values()

        # Specify the Django template and provide data context
    template = 'users/list_with_favs.html'
    context = {
        'favstore_list': list_of_users_with_favs
    }

    return render(request, template, context)      

