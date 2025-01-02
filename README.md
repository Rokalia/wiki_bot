Этот проект предназначен для автоматизации поика по википедии. Выполняется в Google Colab в режиме GPU.
Создайте Colab проект и клонируйте репозиторий.
Затем вставьте токен от созданного вами telegram бота в bot.py.\n
Запустите в Colab следующий код:\n
%cd wiki_bot\n
!pip install -r requirements.txt\n
!python bot.py\n
\n
Когда вывод покажет :"Device set to use cuda", то ботом можно пользоваться.\n
