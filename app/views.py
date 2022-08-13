from django.shortcuts import render
import telegram

# Create your views here.


def copy_message(request):

    if request.method == "POST":
        send_message = '@' + request.POST['send_message']
        copy_message = '@' + request.POST['copy_message']
        bot_token = request.POST['bot_token']
        
        auth = telegram.Bot(token=bot_token)
        print('Bot ishga tushdi')
        
        b = 3

        def forward(send_message, copy_message, b, auth):
            print(send_message)
            print(copy_message)
            print(bot_token)
            
            try:
                for msg in range(b, 1401):
                    telegram.Bot.forwardMessage(auth, chat_id=send_message, from_chat_id=copy_message, message_id=msg)
                    print('Ishlamoqda')

            except telegram.error.BadRequest:
                b = msg + 1
                forward(send_message, copy_message, b, auth)

            print('Xabarlar Ko\'chirildi')
        
        forward(send_message, copy_message, b, auth)

    return render(request, 'index.html')