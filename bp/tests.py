from django.test import TestCase

# Create your tests here.
<html lang="en">
<head>

  {% block title %}<title>Local Site</title>{% endblock %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  {% load static %}
  <link rel="stylesheet" href="{% static 'bp/styles.css' %}">
</head>

<body>

  <div class="container-fluid">

    <div class="row">
      <div class="col-sm-2">
      {% block sidebar %}
      <ul class="sidebar.nav">
        <br>
        <li><a href="studentmenu/">STUDEN_MENU</a></li>
        <li><a href="exercises/">exercises_list</a></li>
        <hr>
        <li><a href="accounts/login/">TEACHER_MENU</a></li>
        <li><a href="videos/upload/">Video</a></li>
        <li><a href="admin/bp/exercises/">Exercises</a></li>
        <hr>
        <li><a href="admin/">admin page</a></li>
        {% if user.is_authenticated %}
            <li>User:{{ user.get_username }}</li>
            <li><a href="{% url 'logout'%}?next={{request.path}}">logout</a></li>
        {% else %}
            <li><a href="{% url 'login'%}?next={{request.path}}">login</a></li>
        {% endif %}
      </ul>
      {% endblock %}
      </div>
    </div>

  </div>

</body>
</html>
