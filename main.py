from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Sekretne klucz do obsługi sesji

questions = [
    {
        "question": "Jak nazywam cię najczęściej zdrobniale?",
        "options": ["Kochanie", "Skarbie", "Kruszynko", "Kiciu"],
        "correct_answer": "Skarbie"
    },
    {
        "question": "Jaki jest mój ulubiony kolor?",
        "options": ["Czerwony", "Niebieski", "Czarny", "Zielony"],
        "correct_answer": "Zielony"
    },
    {
        "question": "Gdzie chciałbym z tobą zamieszkać?",
        "options": ["W mieście", "Na wsi", "Domek przy lesie", "W lepiance"],
        "correct_answer": "Domek przy lesie"
    },
    {
        "question": "Jaki jest mój ulubiony styl ubierania się?",
        "options": ["Menel-style", "Elegancja-Francja", "Modnie", "Co pierwsze sie nawinie w szafie"],
        "correct_answer": "Menel-style"
    },
    {
        "question": "Co mówię do ciebie jako wyraz miłości?",
        "options": ["Spierdalaj", "Lofciam cie", "Kocham cie", "Tęsknie"],
        "correct_answer": "Spierdalaj"
    },
    {
        "question": "Jaki jest mój ulubiony gatunek filmowy?",
        "options": ["Dramat", "Horror", "Akcja", "Komedia", "Romantyczny"],
        "correct_answer": "Komedia"
    },
    {
        "question": "Jakiego rodzaju filmów nie lubię oglądać?",
        "options": ["Dramat", "Horror", "Romantyczny"],
        "correct_answer": "Romantyczny"
    },
    {
        "question": "Jakie jest moje aktualne marzenie, które chciałbym zrealizować z tobą?",
        "options": ["Oświadczyć sie", "Zerwać", "Zamieszkać razem"],
        "correct_answer": "Zamieszkać razem"
        },
    {
        "question": "Który z nas częściej organizuje niespodzianki dla drugiej osoby?",
        "options": ["Jakub", "Marysia"],
        "correct_answer": "Nie ma to znaczenia, bo liczy się to że sie oboje kochamy"
    },
    {
        "question": "Jaki jest mój ulubiony napój?",
        "options": ["Pepsi", "Coca-Cola", "Fanta", "Mirinda"],
        "correct_answer": "Mirinda"
    },
    {
        "question": "Co najbardziej lubię robić z tobą podczas wolnego czasu?",
        "options": ["Oglądać filmy", "Grać w gierki", "Śpiewać", "Bawić sie", "Wszystkie powyższe"],
        "correct_answer": "Wszystkie powyższe"
    },
    {
        "question": "Jaki jest mój ulubiony rodzaj muzyki?",
        "options": ["Rap", "Trap", "Hip-Hop", "Disco-polo", "Phonk"],
        "correct_answer": "Hip-Hop"
    },
    {
        "question": "Które z nas częściej przygotowuje śniadania?",
        "options": ["Oczywiście że ja :P", "Ty",],
        "correct_answer": "Oczywiście że ja :P"
        },
    {
        "question": "Które z nas jest bardziej romantyczne?",
        "options": ["Jakub", "Marysia"],
        "correct_answer": "Marysia"
    },
    {
        "question": "Co najbardziej cenię w naszym związku?",
        "options": ["Szacunek", "Wsparcie", "Lojalność", "Miłość"],
        "correct_answer": "Lojalność"
    },
    {
        "question": "Które z nas zazwyczaj wybiera filmy do oglądania?",
        "options": ["Jakub", "Marysia"],
        "correct_answer": "Marysia"
    },
    {
        "question": "Co najbardziej lubię w naszych wspólnych przejażdzkach?",
        "options": ["Prędkość", "Miejsce docelowe", "Wspólne śpiewanie", "Ananas"],
        "correct_answer": "Wspólne śpiewanie"
    },
    {
        "question": "Co jest moim ulubionym wspomnieniem z naszego pierwszego spotkania?",
        "options": ["Pocałunek", "Szukanie apartamentu", "Poznanie twojego brata", "Ty w bieliźnie", "Twoja obecność"],
        "correct_answer": "Twoja obecność"
    },
    {
        "question": "Jakie jest moje ulubione hobby?",
        "options": ["Śpiewanie", "Rysowanie", "Robienie grafik", "Motoryzacja", "Kodowanie", "Animowanie", "Obróbka Video", "Kurwa za dużo ich masz"],
        "correct_answer": "Kurwa za dużo ich masz"
    },
    {
        "question": "Jaki jest mój ulubiony sposób na relaks po ciężkim dniu?",
        "options": ["Gierkowanie", "Wylegiwanie się", "Jazda samochodem", "Walenie konia"],
        "correct_answer": "Wylegiwanie się"
    },
    {
        "question": "Co najbardziej lubię robić z tobą w domu?",
        "options": ["Leżeć", "Gotować", "Ruchać sie", "Oglądać filmy", "Grać", "Miziać sie"],
        "correct_answer": "Gotować"
    },
    {
        "question": "Jaki jest mój ulubiony prezent, który dostałem od ciebie?",
        "options": ["Klocki Lego", "Guma na chuja", "Breloczek spier-mana", "Perfumy", "Myszka", "Żel do miejsc intymnych"],
        "correct_answer": "Perfumy"
    },
    {
        "question": "Jaka jest moja ulubiona rzecz, którą robię dla ciebie?",
        "options": ["Prezenty", "Zaskakiwanie cię", "Zdjęcia", "Ruchanie"],
        "correct_answer": "Zaskakiwanie cię"
        },
    {
        "question": "Co najbardziej cenię w twojej obecności?",
        "options": ["Robienie loda", "Całuski", "Po prostu twoja obecność", "Przytulanie"],
        "correct_answer": "Po prostu twoja obecność"
    },
    {
        "question": "Co najbardziej lubię w twoim sposobie okazywania mi miłości?",
        "options": ["Szczerość", "Kreatywność", "Podejście", "Uczucie"],
        "correct_answer": "Szczerość"
    },
    {
        "question": "Co najbardziej mnie kręci w twojej sylwetce?",
        "options": ["Piersi", "Tyłek", "Charakter", "Cipcia", "Brzuszek"],
        "correct_answer": "Cała jesteś wspaniała i wszystko mi sie podoba <3"
    },
    {
        "question": "Co najbardziej cenię w naszej codziennej rutynie?",
        "options": ["Pisanie na dzień dobry", "Pisanie na dobranoc", "Spędzanie czasu podczas dnia", "Wszystko powyższe"],
        "correct_answer": "Wszystko powyższe"
    },
    {
        "question": "Jakie jest moje ulubione miejsce na romantyczny piknik?",
        "options": ["Polana", "Las", "Plaża", "Park"],
        "correct_answer": "Polana"
        },
    {
        "question": "Kochasz mnie?",
        "options": ["Tak"],
        "correct_answer": "Tak"
    },
    {
        "question": "Na pewno?",
        "options": ["Tak"],
        "correct_answer": "Tak"
    },
    {
        "question": "Jesteś pewna?",
        "options": ["Tak"],
        "correct_answer": "Tak"
    },
    {
        "question": "Zostaniesz ze mną na zawsze?",
        "options": ["Tak"],
        "correct_answer": "Tak"
    },
    {
        "question": "Ostatnie pytanie znajduje się na końcu quizu!",
        "options": ["OK"],
        "correct_answer": "OK"
    },
    
]

current_question_index = 0  # Indeks aktualnego pytania
score = 0  # Zmienna przechowująca wynik quizu

@app.route("/", methods=["GET", "POST"])
def index():
    global current_question_index, score

    if request.method == "POST":
        answer = request.form.get("answer")
        correct_answer = questions[current_question_index]["correct_answer"]

        if answer == correct_answer:
            score += 1  # Zwiększ punktację o 1 za poprawną odpowiedź

        current_question_index += 1  # Przejdź do następnego pytania

        if current_question_index >= len(questions):
            return redirect(url_for("end", score=score))  # Przekazujemy score do funkcji end()

    if current_question_index < len(questions):
        return render_template("index.html", current_question=questions[current_question_index])
    else:
        return redirect(url_for("end", score=score))

@app.route("/end")
def end():
    total_questions = len(questions)
    return render_template("end.html", score=score, total_questions=total_questions, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
