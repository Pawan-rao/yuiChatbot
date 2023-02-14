import nltk
from nltk.chat.util import Chat,reflections


set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today?",]
    ],
    [
        r"hi|hello|hey|yo|wassup?",
        ["hello","hi","yo bro","Hey there",]
    ],
    [
        r"How are you doing today?",
        ["I am just fine, thank you for asking",]
    ],
    [ 
        r"who are you?|introduce yourself",
        ["I am YUI, a rulebased chatbot created by Pawan S Rao. I am here to help you in any way possible :)"]
    ],
    [ 
        r"Quit|Bye|See ya|tata",
        ["Bye, take care see you soon :)","It was nice chatting with you"]
    ]
]


