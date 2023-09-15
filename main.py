from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hello = """Welcome to GameBot.
Here you can play some minigames.
INSTRUCTION:
ENG:
You are playing against a robot and you have to overplay him in minigames.
1. Tap on a game you want to play, the first sticker is sent automatically and it's bot's turn.
2. You have to send the same sticker 
    2.1 ... by typing the name of a game into text field and clicking an icon above.
    2.2 ... by forwarding a sticker that was sent to the chat with bot.
3. Type "/help" to see commands's meaning.
Good luck!
UKR:
Ви граєте проти робота і вам потрібно його виграти в мінігрі.
1. Нажміть на гру в яку ви хочете пограти, перша наліпка відправлена автоматично, це був хід телеграм боту.
2. Наступний хід ваш, щоб відправити такий самий стікер
    2.1... введіть назву гри без слешу, а просто назву без пробілів або ще чогось, вам має зверху з'явитися плашка з наліпкою
    2.2... виділіть стікер надісланий ботом і перешліть його в той самий чат.
3. Введіть "/help" щоб дізнатися значення команд-кнопок.
Хай щастить!"""


HELP_COMMAND = """
/help - command list
/start - restart
/dart - throw a dart
/dice - throw a dice
/basketball - play basketball
/football - play football
/bowling - play bowling
/casino - play casino
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add('/help','/dart','/dice').add('/basketball','/football','/bowling','/casino')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=hello, reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['dice'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice()
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        await message.answer(text="It's my turn:")
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text='You won🥳')
        elif user_val == val:
            await message.answer(text="That's a tie")
        else:
            await message.answer(text="Haha, you lost!💩💩")

@dp.message_handler(commands=['dart'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice(emoji='🎯')
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text='You won. Bullseye🥳!')
        elif user_val == val:
            await message.answer(text="That's a tie😐")
        else:
            await message.answer(text="Haha, you lost!💩💩")

@dp.message_handler(commands=['basketball'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice(emoji='🏀')
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text="You won. That's a 3-pointer🥳!")
        elif user_val == val:
            await message.answer(text="That's a tie😐")
        else:
            await message.answer(text="Haha, you lost!💩💩")

@dp.message_handler(commands=['football'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice(emoji='⚽')
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text='You won. Ciuuu🥳!')
        elif user_val == val:
            await message.answer(text="That's a tie😐")
        else:
            await message.answer(text="Haha, you lost!💩💩")

@dp.message_handler(commands=['bowling'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice(emoji='🎳')
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text="You won. That's a strike!🥳")
        elif user_val == val:
            await message.answer(text="That's a tie😐")
        else:
            await message.answer(text="Haha, you lost!💩💩")

@dp.message_handler(commands=['casino'])
async def dice(message: types.Message):
    await message.answer(text="It's my turn:")
    msg = await message.reply_dice(emoji='🎰')
    await message.answer(text="It's your turn now. Please, send the same sticker.")
    val = msg.dice.value
    print(val)
    await message.delete()

    @dp.message_handler(content_types=types.ContentType.DICE)
    async def handle_dice(message: types.Message):
        user_val = message.dice.value
        print(user_val)
        if user_val > val:
            await message.answer(text='You won. You are a lucky guy🥳!')
        elif user_val == val:
            await message.answer(text="That's a tie😐")
        else:
            await message.answer(text="Haha, you lost!💩💩")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

