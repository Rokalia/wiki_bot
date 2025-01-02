Этот проект предназначен для автоматизации поика по википедии. Выполняется в Google Colab в режиме GPU.  
Создайте Colab проект и клонируйте репозиторий.  
Затем вставьте токен от созданного вами telegram бота в bot.py.  
Запустите в Colab следующий код:  
`%cd wiki_bot  
!pip install -r requirements.txt  
!python bot.py ` 
  
Когда вывод покажет :"Device set to use cuda", то ботом можно пользоваться.
