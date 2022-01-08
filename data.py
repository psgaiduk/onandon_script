from random import choice


def return_settings(level):
    if level < 10:
        time_morning = 30 + 30 * level
        time_inhale = 5
        time_delay = 3
        time_exhalation = 5
    else:
        time_morning = 300
        if level < 20:
            time_inhale = 5 + level - 9
            time_delay = 3 + level - 9
            time_exhalation = 5 + level - 9
        else:
            time_inhale = 15
            time_delay = 13
            time_exhalation = 15

    time_self_development = 30
    abs_exercises_with_info = [
        {'Альпинист': "Примите упор лёжа. Подтяните правое колено к груди, выпрыгните и поменяйте в воздухе ноги - "
                      "левую вперёд, правую назад."},
        {'Велосипед': "Лягте на спину, положите руки под голову, поднимите колени и крутите педали велосипеда\n"
                      "Затем начните делать наклоны вперёд, касаясь локтями противоположного колена"},
        {"Двойные скручивания": "Сядьте на пол, отклоните корпус назад и поднимите ноги над полом.\nНайдя точку "
                                "равновесия, поднимите верхнюю часть корпуса и подтяните колени к груди\n"
                                "Вернитесь в исходное положение и повторите упражнение."},
        {"Уголок": "Ложитесь на спину, руки и ноги вытянуты, ноги вместе.\nПоднимите корпус и ноги, коснитесь руками "
                   "носков. Вернитесь в исходное положение и повторите упражнение."},
    ]
    push_exercises_with_info = [
        {'Отжимания': "Примите упор лёжа, руки ровно под плечами, локти близко к корпусу, расстояние между "
                      "ступнями не больше 30 см.\nСгибайте руки в локтях и опускайте тело, пока плечевые части рук не "
                      "будут параллельны полу, затем вернитесь в исходное положение, отжавшись от пола, и повторите"},
        {"Отжимания сидя на полу": "Сядьте на пол, согнув колени и поставив ноги плоско на пол. Поставьте руки на пол "
                                   "под плечами, пальцами по направлению к бёдрам.\nПриподнимите бёдра от пола. Затем"
                                   "сгибайте и разгибайте руки в локтях, чтобы опускать и поднимать бёдра."},
        {"Бёрпи": "Из положения стоя опуститесь на корточки и упритесь руками в землю.\nОдновременно выпрямите руки и"
                  "ноги и сразу же вернитесь в положение на корточках.\nЗатем выпрыгните вверх."},
        {"Гиперэкстензии": "Ложитесь на живот, пальцы ног касаются пола, подбородок лежит на кистях рук.\n"
                           "Поднимите грудь от полка как можно выше. Оставайтесь в этом положении несколько секунд,"
                           "затем вернитесь в исходное положение.\nПовторите упражнение"},
    ]
    foot_exercises_with_info = [
        {"Приседания": "Ноги на ширине плеч, руки вытянуты перед собой. Опускайтесь до тех пор, пока бёдра не будут "
                       "параллельны полу.\nПри выполнении упражнения колени должны быть направлены туда же, куда "
                       "направлены носки ног. Вернитесь в исходное положение."},
        {"Выпады назад": "Встаньте ровно, ноги на ширине плеч, руки на бёдрах.\nСделайте большой шаг назад"
                         "правой ногой, опускаясь всем телом так, чтобы левое бедро было параллельно полу.\n"
                         "Вернитесь в исходное положение и повторите упражнение в другую сторону."},
        {"Подъёмы на стул": "Поставьте правую ногу на стул, затем встаньте на стул обеими ногами. Спуститесь"
                            "со стула (с правой ноги)\nПовторите, теперь начиная с левой ноги."}
    ]

    stretching_exercises_with_info = [
        {'Выпады в сторону': "Встаньте прямо, ноги вместе. Наведите правую ногу в сторону, затем слегка присядьте"
                             "на разогнутую левую ногу.\nВернитесь в обратное положение и перейдите на другую "
                             "сторону."},
        {"Ритм-растяжка спины вперёд": "Садитесь на пол, ступни на ширине плеч, немного опустите подбородок к груди."
                                       "Потянитесь руками вперёд и коснитесь пальцев ног. Вернитесь в исходное "
                                       "положение и повторите.\nТянитесь вперёд на выдохе, возвращайтесь на вдохе."},
        {"Ноги к рукам стоя": "Встаньте ровно, ноги на ширине плеч. Поднимите левую ногу как можно выше и коснитесь её"
                              "правой рукой.\nВернитесь в исходное положение и повторите упражнение в другую сторону."},
        {"Наклон вперёд": "Встаньте ровно, ноги вместе.\nЗатем наклоните корпус вперёд, старясь максимально приблизить"
                          "его к ногам. Оставайтесь в этом положении несколько секунд, затем повторите упражнение."},
        {"Растяжка выпадом вбок": "Встаньте ровно, ноги широко, руки вместе перед грудью.\nОпустите тело и "
                                  "перенесите вес на правую ногу, не сгибая при это левую. "
                                  "Повторите упражнение в другую сторону"},
        {"Бабочка": "Садитесь на пол, ноги вместе. Возьмитесь руками за носки ног.\nРазведите колени в стороны и "
                    "опустите колени как можно ниже."}
    ]

    start_exercises_with_info = [
        {'Прыжки': "Ноги вместе, руки вдоль корпуса. Прыжком разведите ноги, одновременно поднимая руки в стороны до"
                   "положения над головой. Прыжком верните в исходное положение."}
    ]

    exercises = [
        choice(start_exercises_with_info),
        choice(push_exercises_with_info),
        choice(abs_exercises_with_info),
        choice(foot_exercises_with_info),
        choice(stretching_exercises_with_info),
        choice(stretching_exercises_with_info),
                 ]

    if level < 4:
        time_exercises = 40 + 5 * level
        time_relax = 6 + 1 * level
    else:
        time_exercises = 60
        time_relax = 10

    return {
        "time_morning": time_morning,
        "time_self_development": time_self_development,
        "exercises": exercises,
        "time_exercises": time_exercises,
        "time_relax": time_relax,
        "time_inhale": time_inhale,
        "time_delay": time_delay,
        "time_exhalation": time_exhalation,
    }