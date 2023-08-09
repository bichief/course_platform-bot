import {useCallback} from "react";
import styles from "./Rates.module.css";
import {useNavigate} from "react-router-dom";

const Rates = () => {
    const navigate = useNavigate()
    const onBackButtonIconClick = useCallback(() => {
        navigate('/')
    }, []);

    const onButtonContainerClick = useCallback(() => {
        const anchor = document.querySelector(
            "[data-scroll-to='priceBlockContainer']"
        );
        if (anchor) {
            anchor.scrollIntoView({block: "start", behavior: "smooth"});
        }
    }, []);

    return (
        <div className={styles.rates}>
            <div className={styles.upderTop1}/>
            <img
                className={styles.backButtonIcon1}
                alt=""
                src="/back-button.svg"
                onClick={onBackButtonIconClick}
            />
            <div className={styles.priceblock}>
                <div
                    className={styles.priceblock1}
                    data-scroll-to="priceBlockContainer"
                >
                    <img
                        className={styles.priceBlockBackgroundIcon}
                        alt=""
                        src="/price-block-background.svg"
                    />
                    <div className={styles.div}>
            <span className={styles.txt}>
              <p className={styles.p}>Сколько стоят</p>
              <p className={styles.p}>новые возможности?</p>
            </span>
                    </div>
                    <b className={styles.b}>
            <span className={styles.txt}>
              <p className={styles.p2}>65 уроков + 40 домашних заданий</p>
              <p className={styles.p}>Зум-сессии раз в неделю</p>
              <p className={styles.p4}>Готовый проект в портфолио</p>
              <p className={styles.p}>Общий чат курса со спикером</p>
              <p className={styles.p6}>Получение заказов на чат-ботов</p>
              <p className={styles.p}>Доступ в закрытый канал</p>
              <p className={styles.p}>Вебинары на выбранную тему</p>
            </span>
                    </b>
                    <div className={styles.div1}>
            <span className={styles.txt}>
              <span>12000</span>
              <span className={styles.span}>₽</span>
            </span>
                    </div>
                </div>
            </div>
            <div className={styles.buybutton}>
                <div className={styles.buybutton1}>
                    <div className={styles.buyButtonBackground1}/>
                    <div className={styles.div2}>ЗАПИСАТЬСЯ НА КУРС</div>
                </div>
            </div>
            <div className={styles.rate1}>
                <div className={styles.rate11}>
                    <img
                        className={styles.mainBackgroundRateIcon}
                        alt=""
                        src="/main-background-rate.svg"
                    />
                    <div className={styles.inmoduleParent}>
                        <div className={styles.inmodule}>
                            <img
                                className={styles.inModuleBackgroundIcon}
                                alt=""
                                src="/in-module-background.svg"
                            />
                            <b className={styles.b1}>Вводный модуль</b>
                            <div className={styles.pycharmContainer}>
                <span className={styles.txt}>
                  <p className={styles.p}>Урок 1. Знакомство</p>
                  <p className={styles.p}>
                    Урок 2. Учимся работать с платформой
                  </p>
                  <p className={styles.p}>Урок 3. Система рейтинга в курсе</p>
                  <p className={styles.p}>Урок 4. Что такое Боты</p>
                  <p className={styles.p}>Урок 5. Основные виды чат-ботов</p>
                  <p className={styles.p}>
                    Урок 6. Где зарабатывают разработчики?
                  </p>
                  <p className={styles.p}>
                    Урок 7. Подготовка. Программы для работы
                  </p>
                  <p className={styles.p}>
                    Урок 8. PyCharm. Лайфхаки и основны
                  </p>
                  <p className={styles.p}>
                    Урок 9. Git. Система контроля версий
                  </p>
                </span>
                            </div>
                        </div>
                        <div className={styles.pythonmodule}>
                            <img
                                className={styles.pythonModuleBackgroundIcon}
                                alt=""
                                src="/python-module-background.svg"
                            />
                            <b className={styles.python1}>Python модуль</b>
                            <div className={styles.pythonContainer}>
                <span className={styles.txt}>
                  <p className={styles.p}>
                    Урок 1. Python - знакомство с языком
                  </p>
                  <p className={styles.p}>
                    Урок 2. Переменные. Вводить/вывод своего имени
                  </p>
                  <p className={styles.p}>Урок 3. Типы данных. Строки, числа</p>
                  <p className={styles.p}>Урок 4. Условия, если-иначе</p>
                  <p className={styles.p}>
                    Урок 5. Циклы for/while. Их особенности
                  </p>
                  <p className={styles.p}>Урок 6. Строки. Методы и фишки</p>
                  <p className={styles.p}>Урок 7. Списки и их методы</p>
                  <p className={styles.p}>
                    Урок 8. Словарь. Учимся работать с JSON
                  </p>
                  <p className={styles.p}>
                    Урок 9. Функции в Python: что это такое?
                  </p>
                  <p className={styles.p}>Урок 10. Обычные функции</p>
                  <p className={styles.p}>
                    Урок 11. Лямбда и возвратные функции
                  </p>
                  <p className={styles.p}>Урок 12. Введение в ООП</p>
                  <p className={styles.p}>Урок 13. Классы в Python</p>
                </span>
                            </div>
                        </div>
                        <div className={styles.aiogrammodule}>
                            <img
                                className={styles.aiogramModuleBackgroundIcon}
                                alt=""
                                src="/aiogram-module-background.svg"
                            />
                            <b className={styles.aiogram}>Aiogram модуль</b>
                            <div className={styles.aiogram2Container}>
                                <p className={styles.p}>Урок 1. Знакомство с Aiogram</p>
                                <p className={styles.p}>Урок 2. Понятие асинхронности</p>
                                <p className={styles.p}>
                                    Урок 3. Знакомство с Темплейтом, его понятие
                                </p>
                                <p className={styles.p}>
                                    Урок 4. Связываем Telegram с кодом. Первый бот
                                </p>
                                <p className={styles.p}>Урок 5. Работа с Фильтрами</p>
                                <p className={styles.p}>
                                    Урок 6. Клавиатуры, их виды и возможности
                                </p>
                                <p className={styles.p}>Урок 7. Inline mode</p>
                                <p className={styles.p}>Урок 8. Способы отправки сообщений</p>
                                <p className={styles.p}>
                                    Урок 9. Взаимодействие с медиа-файлами
                                </p>
                                <p className={styles.p}>Урок 10. Машина состояний</p>
                            </div>
                        </div>
                        <div className={styles.dbmodule}>
                            <img
                                className={styles.dbModuleBackgroundIcon}
                                alt=""
                                src="/db-module-background.svg"
                            />
                            <b className={styles.b2}>База Данных</b>
                            <div className={styles.crudContainer}>
                <span className={styles.txt}>
                  <p className={styles.p}>Урок 1. База Данных: что это?</p>
                  <p className={styles.p}>
                    Урок 2. Настраиваем и подключаем БД
                  </p>
                  <p className={styles.p}>{`Урок 3. Создание таблиц `}</p>
                  <p className={styles.p}>Урок 4. CRUD операции с БД</p>
                  <p className={styles.p}>
                    Урок 5. SQLAlchemy. Знакомство с ORM-системами
                  </p>
                  <p className={styles.p}>
                    Урок 6. Django. Создаем админ-панель
                  </p>
                </span>
                            </div>
                        </div>
                        <div className={styles.servermodule}>
                            <img
                                className={styles.serverModuleBackgroundIcon}
                                alt=""
                                src="/server-module-background.svg"
                            />
                            <b className={styles.b3}>Работа с сервером</b>
                            <div className={styles.div3}>
                <span className={styles.txt}>
                  <p className={styles.p}>Урок 1. Выбираем сервер для бота</p>
                  <p className={styles.p}>
                    Урок 2. Учимся взаимодействовать с сервером через Командную
                    строку
                  </p>
                  <p className={styles.p}>
                    Урок 3. Способы загрузки бота на сервер
                  </p>
                  <p className={styles.p}>
                    Урок 4. Вносим правки в бота для корректной работы
                  </p>
                  <p className={styles.p}>
                    Урок 5. Как запустить бота на сервере?
                  </p>
                </span>
                            </div>
                        </div>
                        <div className={styles.bonusmodule}>
                            <img
                                className={styles.bonusModuleBackgroundIcon}
                                alt=""
                                src="/bonus-module-background.svg"
                            />
                            <b className={styles.b4}>Бонус</b>
                            <div className={styles.div4}>
                                <p className={styles.p}>Урок 1. Где найти первых клиентов?</p>
                                <p className={styles.p}>Урок 2. Как общаться с клиентами?</p>
                                <p className={styles.p}>Урок 3. Как правильно составить ТЗ?</p>
                                <p className={styles.p}>
                                    Урок 4. Как лучше всего оформить кейсы?
                                </p>
                                <p className={styles.p}>
                                    Урок 5. Учимся собирать (парсить) данные с сайтов
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.bonuscourse}>
                <div className={styles.bonuscourse1}>
                    <img
                        className={styles.bonusCourseBackgroundIcon}
                        alt=""
                        src="/bonus-course-background.svg"
                    />
                    <b className={styles.b5}>Плюшки курса</b>
                    <div className={styles.div5}>
            <span className={styles.txt}>
              <p className={styles.p}>
                <b className={styles.b6}>-</b>
                <span className={styles.b6}>{` `}</span>
                <b className={styles.b6}>Пожизненный доступ в закрытый канал</b>
                <span> с материалами, которые не попали в основной курс</span>
              </p>
              <p className={styles.p}>
                <b className={styles.b6}>- Зум-сессии с разбором вопросов</b>
                <span>{` раз в неделю во время обучения `}</span>
              </p>
              <p className={styles.p}>
                <b className={styles.b6}>- Доступ к вебинарам</b>
                <span> на выбранную тематику</span>
              </p>
            </span>
                    </div>
                    <div className={styles.button} onClick={onButtonContainerClick}>
                        <div className={styles.backgroudMoreButton1}/>
                        <b className={styles.b10}>ПОДРОБНЕЕ</b>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Rates;
