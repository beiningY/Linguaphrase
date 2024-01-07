import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monProjet.settings')
django.setup()

from myApp.models import Word  

color_examples = {
    "black": ["Her cat has black fur.", "The night sky is so dark it's almost black."],
    "blue": ["The clear sky is a beautiful shade of blue.", "He painted his room a bright blue color."],
    "brown": ["The dog's fur is brown.", "She likes to wear brown shoes with her jeans."],
    "green": ["The grass in the park is a vibrant green.", "He planted green beans in his garden."],
    "grey": ["The clouds on a rainy day are often grey.", "His new car is painted in grey."],
    "orange": ["There is an orange table.", "She wore an orange dress to the party."],
    "pink": ["The flowers in the garden are a lovely shade of pink.", "He gave her a pink rose as a token of his affection."],
    "purple": ["Your purple lipstick suits you nicely.", "She painted her bedroom walls in a soft purple color."],
    "red": ["The firetruck is bright red.", "She loves to wear red lipstick."],
    "violet": ["Some flowers are a deep violet color.", "The sunset had beautiful shades of violet."],
    "white": ["Snow is pure white in the winter.", "Her wedding dress was a stunning white gown."],
    "yellow": ["Sunflowers are known for their bright yellow petals.", "The school bus is yellow."],
}

color_verbs_data = {
    "like": {
        "definition": "To have a preference or enjoy something.",
        "examples": ["I like chocolate ice cream.",
                     "She likes the color blue."],
        "image_url": "https://cdn-icons-png.flaticon.com/256/1175/1175578.png",
    },
    # Add more verbs in a similar format
    "color": {
        "definition": "To add or apply color to something; to give hue, tint, or shade.",
        "examples": ["Children enjoy coloring pictures with crayons.",
                     "She colored her hair with a bright shade of blue."],
        "image_url": "https://bustedhalo.com/wp-content/uploads/2016/06/bigstock-Image-Of-Woman-Coloring-Adult-131600813-325x216.jpg"
    },
            
    "dye": {
        "definition": "To change the color of something, especially fabric or hair, using a coloring substance.",
        "examples": ["She decided to dye her T-shirt a different color.",
                     "He dyed his hair black for a new look."],
        "image_url": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/5._making_tie-dye_clothes-ad67d30.jpg?quality=90&fit=700,350"
    },

    "paint": {
        "definition": "To apply color to a surface using a brush or other tool.",
        "examples": ["She likes to paint her bedroom walls in vibrant colors.",
                     "He painted his car red."],
        "image_url": "https://www.your-decorative-painting-resource.com/images/iStockPaintTechniques.jpg"
    },
}

town_examples = {
    "bank": ["I need to go to the bank to withdraw some cash.", "My mom works at the bank down the street."],
    "church": ["We go to church every Sunday for worship.", "You can pray to God in church."],
    "cinema" : ["We went to the cinema to watch a movie.", "They sell popcorn and candy at the cinema."],
    "gas station" : ["I need to stop at the gas station to fill up the car.", "I parked my car at the gas station."],
    "hospital" : ["She was taken to the hospital when she got sick.", "The hospital has a great team of doctors."],
    "library" : ["I like to study at the library after school.", "You can borrow books at the library for free."],
    "museum" : ["The museum has a fascinating dinosaur exhibit.", "We visited the art museum over the weekend."],
    "post office" : ["I need to mail this letter at the post office.", "The post office is closed on Sundays."],
    "restaurant" : ["Let's go to a restaurant for dinner tonight.", "They serve delicious pasta at the Italian restaurant."],
    "school" : ["I walk to school every morning with my friends.", "The school year begins in September."],
    "supermarket" : ["I'm going to the supermarket to buy groceries.", "The supermarket is having a sale on fruits and vegetables."],
    "theatre" : ["We're going to the theatre to watch a play.", "The theatre is known for its amazing performances."]
}

town_verbs_data = {
    "watch": {
        "definition": "To look at or observe attentively, typically for enjoyment or information.",
        "examples": ["He likes to watch movies at the cinema.",
                     "She watches tv shows everyday."],
        "image_url": "https://www.shutterstock.com/image-photo/little-boy-beautiful-young-woman-260nw-101431642.jpg",
    },
    # Add more verbs in a similar format
    "visit": {
        "definition": "To go to a place, such as a town, for a purpose like sightseeing or exploring.",
        "examples": ["Tourists like to visit the historic landmarks in the town.",
                     "She visited the local museum to learn about its exhibits."],
        "image_url": "https://eslconversationtopics.com/wp-content/uploads/2023/03/allkj292joq.jpg"
    },

    "eat": {
        "definition": "To consume food by putting it into one's mouth and swallowing.",
        "examples": ["They decided to eat dinner at their favorite restaurant.",
                     "In the morning, she likes to eat a healthy breakfast."],
        "image_url": "https://quizizz.com/media/resource/gs/quizizz-media/quizzes/cde7f6d7-a0f1-4283-90d4-84505dbb4fb4"
    },

    "shop": {
        "definition": "To visit stores and purchase goods or services.",
        "examples": ["They like to shop for groceries at the local supermarket.",
                     "She shops for clothes in the town's shopping district."],
        "image_url": "https://1.bp.blogspot.com/-cAm7wTseOWI/UYl1U3OuySI/AAAAAAAAABg/x4F9PYAVdoE/s1600/shopping1.jpg"
    },

}

kitchen_examples = {
    "cooker": ["I'm using the cooker to make dinner tonight.", "The electric cooker in the kitchen is very efficient."],
    "cup": ["Can you pass me a cup of coffee, please?", "I accidentally dropped my cup, and it broke."],
    "fork" : ["Use a fork to eat your spaghetti.", "I'll grab a fork for the salad."],
    "fridge" : ["The milk goes in the fridge to keep it cold.", "I need to clean out the fridge; it's getting crowded."],
    "kettle" : ["I'm boiling water in the kettle for tea.", "The whistling kettle indicates the water is ready."],
    "knife" : ["Be careful with that sharp knife.", "I need a knife to cut this bread."],
    "mug" : ["I like to drink hot chocolate from my favorite mug.", "He accidentally chipped his favorite mug."],
    "pan" : ["I'm using a frying pan to cook eggs.", "The pan is still hot; be careful."],
    "plate" : ["Put the pizza on a plate.", "I dropped a plate, and it shattered."],
    "pot" : ["I'm making soup in this large pot.", "The pot is heavy when it's full of water."],
    "spoon" : ["Use a spoon to stir the sauce.", "I'll get a spoon for the ice cream."],
    "teapot" : ["She served tea from the beautiful teapot.", "The teapot is a family heirloom."]
}

kitchen_verbs_data = {
    "peel": {
        "definition": "To remove the outer skin or covering from fruits, vegetables, or other foods.",
        "examples": ["He used a peeler to peel the apples for the pie.",
                     "She carefully peeled the potatoes before boiling them."],
        "image_url": "https://i.pinimg.com/564x/b3/08/0f/b3080ffc9817f8552ce1c40a506dc793.jpg"
    },
    # Add more verbs in a similar format
    "bake": {
        "definition": "To cook food, especially bread and pastry, by dry heat in an oven.",
        "examples": ["She decided to bake cookies for the school bake sale.",
                     "The aroma of freshly baked bread filled the kitchen."],
        "image_url": "https://media.baamboozle.com/uploads/images/130509/1601843703_49217"
    },
    
    "mix": {
        "definition": "To combine different ingredients or substances to form a uniform product.",
        "examples": ["In baking, it's important to mix the ingredients thoroughly.",
                     "He likes to mix various fruits in his morning smoothie."],
        "image_url": "https://as1.ftcdn.net/v2/jpg/02/87/67/96/1000_F_287679621_UWDMEajuCdkZCnbBjXreTSToGaKFwiHH.jpg"
    },

    "cook": {
        "definition": "To prepare food for eating by applying heat, often using various ingredients and techniques.",
        "examples": ["She likes to cook delicious meals for her family.",
                     "He learned to cook different cuisines during quarantine."],
        "image_url": "https://www.learnamericanenglishonline.com/wp-content/uploads/all_img/wok%20stir%20fry.jpg"
    },
}

pencase_examples = {
    "clips": ["I need some clips to keep these papers together.", "She used colorful clips to organize her notes."],
    "crayons": ["Children enjoy coloring with crayons.", "The box of crayons had all the colors of the rainbow."],
    "eraser" : ["I used an eraser to correct my mistake.", "My eraser is getting worn down from all the drawing."],
    "glue" : ["Can you pass me the glue for my art project?", "The glue is still wet; be careful not to smudge it."],
    "paintbrush" : ["The artist selected a fine paintbrush for delicate work.", "I need a paintbrush to complete this painting."],
    "paints" : ["The paints are in the art supplies drawer.", "She mixed her paints to create a new color."],
    "pen" : ["I always carry a pen in my pocket.", "The teacher uses a red pen to grade papers."],
    "pencil" : ["I prefer using a pencil because it's easy to erase mistakes.", "The pencil lead broke when I was writing."],
    "ruler" : ["Use a ruler to draw straight lines.", "I can't find my ruler for geometry class."],
    "scissors" : ["I need scissors to cut this paper.", "Be careful with those sharp scissors."],
    "sharpener" : ["The pencil sharpener is on the desk.", "I had to sharpen my kitchen knife before slicing the vegetables."],
    "tape" : ["Can you hand me the tape to wrap this gift?", "I used duct tape to fix the broken handle on my suitcase."]
}

pencase_verbs_data = {
    "store": {
        "definition": "To keep or accumulate supplies, such as pens and pencils, in a designated place.",
        "examples": ["She stores a variety of pens in her pencase.",
                     "It's convenient to store writing tools in a pencase."],
        "image_url": "https://thumbs.dreamstime.com/b/woman-sitting-floor-waste-moving-boxes-her-apartement-37051378.jpg"
    },
    # Add more verbs in a similar format
    "write": {
        "definition": "To trace or form characters on the surface of some material, as with a pen or pencil.",
        "examples": ["She likes to write notes in her pencase.",
                     "Students are required to write essays for their assignments."],
        "image_url": "https://static.javatpoint.com/definition/images/verb-definition3.png"
    },
    
    "sketch": {
        "definition": "To make a rough drawing or outline with a pencil or pen.",
        "examples": ["Artists often sketch in their pencase before creating final artworks.",
                     "She sketched a quick doodle during the meeting."],
        "image_url": "https://cdn.langeek.co/photo/18766/original/sketch"
    },

    "organize": {
        "definition": "To arrange or order items, such as pens and pencils, systematically.",
        "examples": ["He likes to organize his pencase with different compartments.",
                     "It's important to organize your stationary for easy access."],
        "image_url": "https://media.baamboozle.com/uploads/images/55449/1591022431_7117"
    },
}

fruit_examples = {
    "apple": ["An apple is a healthy snack.", "She packed an apple in her lunch for school."],
    "banana": ["Bananas are a great source of energy.", "I usually add sliced banana to my cereal in the morning."],
    "cherry" : ["The pie is filled with sweet, juicy cherries.", "Can you please remove the cherry stems?"],
    "grapes" : ["I enjoy eating grapes during the movie.", "She bought a bunch of green grapes from the grocery store."],
    "lemon" : ["Squeeze some lemon juice over the fish for extra flavor.", "I like my iced tea with a slice of lemon."],
    "orange" : ["I usually have an orange with my breakfast.", "The orange is a citrus fruit with a tangy flavor."],
    "peach" : ["The ripe peach was juicy and delicious.", "I'm going to make a peach cobbler with these peaches."],
    "pear" : ["The pear was perfectly ripe and sweet.", "He took a crisp pear with him as a snack."],
    "pineapple" : ["The tropical fruit salad has chunks of pineapple.", "I like pineapple on my pizza."],
    "plum" : ["The plum tree in the garden is full of fruit.", "This plum is so juicy; it's a delight."],
    "strawberry" : ["Strawberries are my favorite fruit to put on cereal.", "I'm making a strawberry smoothie for breakfast."],
    "watermelon" : ["A slice of watermelon is perfect on a hot summer day.", "We brought a watermelon to the picnic for everyone to share."]
}

fruit_verbs_data = {
    "juice": {
        "definition": "To extract liquid from fruits, often for drinking.",
        "examples": ["They like to juice fresh oranges for a morning drink.",
                     "She juiced a combination of fruits for a nutritious beverage."],
        "image_url": "https://thekitchencommunity.org/wp-content/uploads/2021/12/shutterstock_1938737419-500x500.jpg"
    },
    # Add more verbs in a similar format
    
    "squeeze": {
        "definition": "To apply pressure to extract juice from fruits, often by hand or using a tool.",
        "examples": ["She decided to squeeze lemons for fresh lemonade.",
                     "He squeezed oranges to make homemade orange juice."],
        "image_url": "https://transcode-v2.app.engoo.com/image/fetch/f_auto,c_lfill,h_128,dpr_3/https://assets.app.engoo.com/images/IzCYbzw2CHTF2EDdSod5jqcUmMSa9AmM4uracNP0niA.jpeg"
    },
    
    "pluck": {
        "definition": "To gently pull fruits from a plant or tree, typically by hand.",
        "examples": ["They decided to pluck ripe apples from the tree.",
                     "She carefully plucked berries from the bush."],
        "image_url": "https://www.shutterstock.com/image-photo/ripe-pomegranate-on-branch-female-260nw-1980401213.jpg"
    },

    "inspect": {
        "definition": "To examine fruits closely for quality, ripeness, or defects.",
        "examples": ["Before purchasing, she likes to inspect the fruits for freshness.",
                     "He carefully inspected the peaches for any signs of bruising."],
        "image_url": "https://www.shutterstock.com/image-photo/freshly-harvested-blueberries-fruit-crate-260nw-2170986349.jpg"
    },
}

object_examples = {
    "armchair": ["I like to relax in the armchair with a good book.", "The armchair in the living room is very comfortable."],
    "bed": ["I'm looking forward to a good night's sleep in my cozy bed.", "Can you make the bed with fresh sheets, please?"],
    "bookcase" : ["The bookcase in the study is filled with novels.", "I need more bookcases to store my growing collection."],
    "chair" : ["Please take a seat in the chair while we discuss this.", "The dining room chair has a broken leg."],
    "cupboard" : ["I keep my dishes in the cupboard in the kitchen.", "The cupboard is filled with canned goods."],
    "desk" : ["I do my homework at the desk in my room.", "The office desk is cluttered with papers."],
    "drawers" : ["I store my socks and underwear in these drawers.", "The top drawers are where I keep my jewelry."],
    "shelf" : ["I put the photo frame on the shelf.", "The shelf above the TV is a great place to display collectibles."],
    "sofa" : ["The whole family can sit comfortably on the sofa.", "I like to take a nap on the sofa in the afternoon."],
    "stool" : ["Grab a stool if you want to sit at the kitchen island.", "The stool is lightweight and easy to move around."],
    "table" : ["We gather around the table for family dinners.", "I need a table for my workspace."],
    "wardrobe" : ["My clothes and shoes are in the wardrobe.", "I'm running out of space in the wardrobe."]
}

object_verbs_data = {
    
    "clean": {
        "definition": "To remove dirt, dust, or unwanted substances from surfaces of objects in a room.",
        "examples": ["She decided to clean the living room before guests arrived.",
                     "He cleaned the study room to create a more organized workspace."],
        "image_url": "https://www.shutterstock.com/image-vector/boy-cleaning-floor-mop-260nw-303025817.jpg"
    },
    # Add more verbs in a similar format
    "sit": {
        "definition": "To rest the body on a chair or seat in a room.",
        "examples": ["She likes to sit on the comfortable sofa in the living room.",
                     "He sat at the study desk to complete his homework."],
        "image_url": "https://media.baamboozle.com/uploads/images/289821/1618225994_217221.png"
    },
    
    "open": {
        "definition": "To move or adjust objects to reveal an internal space or contents.",
        "examples": ["He decided to open the curtains in the living room for more sunlight.",
                     "She opened the drawers in the study desk to find her pens."],
        "image_url": "https://i.pinimg.com/originals/d1/48/06/d14806850d605a04e42de0a4320cfff1.jpg"
    },

    "close": {
        "definition": "To move or adjust objects to cover or seal an internal space.",
        "examples": ["She decided to close the windows in the living room as it was getting cold.",
                     "He closed the book after finishing the last chapter in the study room."],
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBPTG5uZZCsy_BgSIFlXKN97J_odGkoVRnD0NXEzmtUoDhyo_zjahaadLL3mly344Urc0&usqp=CAU"
    },
}

pet_examples = {
    "canary": ["The canary chirped melodiously in its cage.", "I love the vibrant yellow color of canaries."],
    "cat": ["My cat loves eating fish.", "He drank a cup of coffee to wake up in the morning."],
    "dog" : ["Our dog loves to go for long walks in the park.", "I'm thinking about getting a dog as a pet."],
    "ferret" : ["The ferret is a playful and curious little animal.", "My cousin has a pet ferret named Sparky."],
    "fish" : ["I have a colorful school of fish in my aquarium.", "The fish in the pond are so pretty."],
    "hamster" : ["My daughter's hamster runs on its wheel all night.", "Hamsters are known for their adorable cheeks."],
    "lizard" : ["I spotted a lizard on the rock.", "The gecko is a type of lizard with a unique appearance."],
    "mouse" : ["I found a tiny mouse in the kitchen.", "We have a new pet mouse."],
    "parrot" : ["The parrot can mimic various sounds and words.", "Parrots are known for their vibrant plumage."],
    "pony" : ["The children love riding the pony at the petting zoo.", "She has a beautiful pony."],
    "rabbit" : ["The rabbit nibbled on the fresh greens in the garden.", "I think a rabbit would make a great pet for the kids."],
    "turtle" : ["The turtle slowly made its way to the pond.", "Turtles are known for their long lifespan."]
}

pet_verbs_data = {
    "pet": {
        "definition": "To stroke or caress an animal, often with affection.",
        "examples": ["She likes to pet her cat when it sits on her lap.",
                     "He petted the dog and gave it a treat."],
        "image_url": "https://merriam-webster.com/assets/ld/word_of_the_day/images/2771/large.jpg"
    },
    # Add more verbs in a similar format
    "play": {
        "definition": "To engage in activities for enjoyment with a pet, involving toys or interaction.",
        "examples": ["They decided to play fetch with their dog in the backyard.",
                     "She plays with her kitten using a string and feather toy."],
        "image_url": "https://images.freeimages.com/clg/istock/previews/1054/105495919-boy-playing-with-dog.jpg"
    },
    
    "feed": {
        "definition": "To provide food or nourishment to a pet.",
        "examples": ["He feeds his fish twice a day.",
                     "She feeds the bird seeds and fruits."],
        "image_url": "https://i.pinimg.com/1200x/9c/e3/54/9ce35442a133e72efc5cb863895902dd.jpg"
    },

    "walk": {
        "definition": "To take a pet outside for exercise, usually on a leash.",
        "examples": ["She walks her dog every morning in the park.",
                     "They decided to walk their rabbit in the backyard on a leash."],
        "image_url": "https://st2.depositphotos.com/38372860/42069/v/450/depositphotos_420693868-stock-illustration-vector-illustration-cartoon-little-boy.jpg"
    },
}

school_examples = {
    "board": ["The teacher wrote the math problem on the board.", "We use a whiteboard to brainstorm ideas in meetings."],
    "book": ["I love to curl up with a good book on a rainy day.", "The library has an extensive collection of books."],
    "calculator" : ["I need a calculator to solve this math problem.", "She always carries a calculator in her backpack."],
    "classroom" : ["The classroom is where we learn new things every day.", "We had a class party in the classroom last week."],
    "diploma" : ["She proudly displayed her diploma on the wall.", "Graduating with a diploma is a significant achievement."],
    "globe" : ["I used a globe to study the countries of the world.", "The globe in the geography classroom is enormous."],
    "map" : ["I unfolded the map to find our way.", "The treasure map led us on an adventure."],
    "notebook" : ["I always take notes in my notebook.", "Her notebook was filled with doodles."],
    "pencase" : ["I keep my pens and pencils in a colorful pencase.", "The pencase fell and scattered pens everywhere."],
    "schoolbag" : ["I packed my schoolbag with books and lunch.", "Her schoolbag is personalized with stickers."],
    "student" : ["Students have to study for exams.", "The student council organizes school events."],
    "teacher" : ["The teacher explained the lesson clearly.", "My favorite teacher is the one who teaches history."]
}

school_verbs_data = {
    
    "listen": {
        "definition": "To pay attention to sounds or information, often in a learning environment like school.",
        "examples": ["She likes to listen to the teacher during class.",
                     "He listened carefully to the instructions given in school."],
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2nKlfhCMNGZGZfVLqxi1a37Ox420sK9j4r62Q3-VgptYrSxtuMrJKyEtUwQn1V8FnYhY&usqp=CAU"
    },
    # Add more verbs in a similar format
    "read": {
        "definition": "To look at and comprehend written words, often in books or on paper.",
        "examples": ["Students read textbooks to understand the lesson.",
                     "She reads a storybook every night before bedtime."],
        "image_url": "https://media.baamboozle.com/uploads/images/3562/1519398595_209240"
    },
    
    "learn": {
        "definition": "To acquire knowledge or skills, often through instruction or study.",
        "examples": ["Students go to school to learn new subjects.",
                     "She enjoys learning about different cultures in geography class."],
        "image_url": "https://c8.alamy.com/compes/2j8r42e/nino-pequeno-de-dibujos-animados-estudiando-en-el-escritorio-2j8r42e.jpg"
    },

    "study": {
        "definition": "To engage in learning or reviewing information, often with the goal of understanding or preparing for an exam.",
        "examples": ["Students need to study for their upcoming tests.",
                     "She studies mathematics every evening to improve her skills."],
        "image_url": "https://static.vecteezy.com/system/resources/previews/005/151/789/non_2x/cartoon-little-boy-studying-on-the-table-free-vector.jpg"
    },
}

summer_examples = {
    "ball": ["We played catch with a colorful ball at the park.", "The soccer ball was nowhere to be found."],
    "crab": ["I saw a crab on the beach.", "We caught crabs in a bucket at the seashore."],
    "hat" : ["I wore a hat to protect my head from the sun.", "His favorite hat is a bright red baseball cap."],
    "hot" : ["It's so hot outside; I need a cold drink.", "Be careful not to touch the hot stove."],
    "ice cream" : ["I enjoy hocolate ice cream for dessert.", "The ice cream truck sells ice cream."],
    "sandcastle" : ["We built a sandcastle on the beach.", "The waves washed away our sandcastle."],
    "shell" : ["I collected seashells on the beach.", "The crab crawled into its shell."],
    "sun" : ["The sun is shining brightly in the sky.", "Don't forget to wear sunscreen in the sun."],
    "sunflower" : ["Sunflowers in the garden sway in the breeze.", "Her sunglasses have stylish frames."],
    "sunglasses" : ["I put on my sunglasses to shield my eyes from the sun.", "I like to talk to my neighbor over the fence."],
    "tent" : ["We slept in a tent in the woods for a camping trip.", "The tent provided shelter from the rain."],
    "umbrella" : ["I brought an umbrella in case it rains.", "The umbrella broke because of the storm."]
}

summer_verbs_data = {
    "have": {
        "definition": "To possess or own something; to be in a specific state or condition.",
        "examples": ["She has a beautiful garden in her backyard.",
                     "They have a new puppy as a pet."],
        "image_url": "https://i0.wp.com/www.flashcardsforkindergarten.com/wp-content/uploads/2021/09/have-verb-flashcard-725x1024.jpg?ssl=1"
    },
    # Add more verbs in a similar format
    "be": {
        "definition": "To exist or have a specific quality or state of being.",
        "examples": ["She wants to be a doctor when she grows up.",
                     "It's important to be happy."],
        "image_url": "https://thumbs.dreamstime.com/z/sweet-little-girl-smiling-teeth-young-happy-sweet-little-girl-smiling-showing-her-white-smile-pointing-fingers-teeth-134153816.jpg"
    },
    
    "drop": {
        "definition": "To let fall or release something from one's hand or a higher position.",
        "examples": ["She accidentally dropped her pen.",
                     "In surprise, he dropped his phone."],
        "image_url": "https://media.baamboozle.com/uploads/images/519540/1648066356_13861.jpeg"
    },

    "look": {
        "definition": "To direct one's gaze in a particular direction or at something.",
        "examples": ["She looked out of the window and admired the view.",
                     "He looked at the painting with interest."],
        "image_url": "https://img.freepik.com/free-vector/active-boy-simple-cartoon-character_1308-105335.jpg"
    },
}

def import_data(theme, url, examples_data, verbs_data):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='boxBox')

    for item in items:
        img_tag = item.find('img', class_='imgBig')
        ul_tag = item.find('ul', class_='kropkiBL-blue666')

        if img_tag and ul_tag:
            img_src = "https://www.anglomaniacy.pl/" + img_tag['src']
            word_text = ul_tag.find_all('li')[0].get_text(strip=True)
            definition_text = ul_tag.find_all('li')[1].get_text(strip=True)
            examples_list = examples_data.get(word_text, ["No example available."])

            word, created = Word.objects.get_or_create(
                word=word_text,
                defaults={
                    'definition': definition_text,
                    'example': ' '.join(examples_list),
                    'image_url': img_src,
                    'category': 'noun',  
                    'theme': theme
                }
            )

    for verb, data in verbs_data.items():
        word, created = Word.objects.get_or_create(
            word=verb,
            defaults={
                'definition': data['definition'],
                'example': ' '.join(data['examples']),
                'image_url': data['image_url'],
                'category': 'verb',
                'theme': theme
            }
        )

themes = [
    {
        "theme": "colours",
        "url": "https://www.anglomaniacy.pl/coloursWordlist.htm",
        "examples_data": color_examples,
        "verbs_data": color_verbs_data
    },
    {
        "theme": "town",
        "url": "https://www.anglomaniacy.pl/townWordlist.htm",
        "examples_data": town_examples,
        "verbs_data": town_verbs_data
    },
    {
        "theme": "kitchen",
        "url": "https://www.anglomaniacy.pl/kitchenWordlist.htm",
        "examples_data": kitchen_examples,
        "verbs_data": kitchen_verbs_data
    },
    {
        "theme": "pencase",
        "url": "https://www.anglomaniacy.pl/pencaseWordlist.htm",
        "examples_data": pencase_examples,
        "verbs_data": pencase_verbs_data
    },
    {
        "theme": "fruits",
        "url": "https://www.anglomaniacy.pl/fruitsWordlist.htm",
        "examples_data": fruit_examples,
        "verbs_data": fruit_verbs_data
    },
    {
        "theme": "objects",
        "url": "https://www.anglomaniacy.pl/furnitureWordlist.htm",
        "examples_data": object_examples,
        "verbs_data": object_verbs_data
    },
    {
        "theme": "pets",
        "url": "https://www.anglomaniacy.pl/petsWordlist.htm",
        "examples_data": pet_examples,
        "verbs_data": pet_verbs_data
    },
    {
        "theme": "school",
        "url": "https://www.anglomaniacy.pl/schoolWordlist.htm",
        "examples_data": school_examples,
        "verbs_data": school_verbs_data
    },
    {
        "theme": "summer",
        "url": "https://www.anglomaniacy.pl/summerWordlist.htm",
        "examples_data": summer_examples,
        "verbs_data": summer_verbs_data
    }
]


for theme in themes:
    import_data(
        theme['theme'],
        theme['url'],
        theme['examples_data'],
        theme['verbs_data']
    )

print("Data import completed!")

