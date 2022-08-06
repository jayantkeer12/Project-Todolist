from django.contrib import admin
from django.urls import path,include
from todoapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect, render    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/home.html',views.LogOut),
    path('todoapp/Verify',views.Verify),
    path('todoapp/Register',views.Register),
    path('todoapp/NewRegister',views.NewRegister),
    path('Verify',views.Verify,name='Verify'),
    path('NewRegister',views.NewRegister,name='NewRegister'),
    path('Register',views.Register,name='Register'),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('todoapp/',views.todoappview),    #/todoapp/
    path('todoappview', views.todoappview,name="todoappview"),
    path('addTodoItem/', views.addTodoItem,name="addTodoItem"),
    path('deleteTodoItem/<int:i>/', views.deleteTodoItem,name="deleteTodoItem"),
    path('password_reset_input_flow_data/',views.Forgot,name="Forgot"),
    path('OTP_confirm',views.Otp_Confirm),
    path('password_reset_input_flow_data/send_gmail',views.send_gmail),
    path('Change_psw',views.Chang_psw),
]
if settings.DEBUG:  
        urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)