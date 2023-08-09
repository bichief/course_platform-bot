import {useCallback} from "react";
import styles from "./Vebinars.module.css";
import {useNavigate} from "react-router-dom";

const Vebinars = () => {
    const navigate = useNavigate()
    const onBackButtonIconClick = useCallback(() => {
        navigate('/')
    }, []);

    return (
        <div className={styles.vebinars}>
            <div className={styles.top}/>
            <img
                className={styles.backButtonIcon}
                alt=""
                src="/back-button.svg"
                onClick={onBackButtonIconClick}
            />
            <div className={styles.vebinarmain}>
                <div className={styles.vebinarmain1}>
                    <div className={styles.mainVebinarBackground}/>
                    <div className={styles.div}>
                        <b>Дата начала:</b>
                        <span className={styles.span}> 01/08/2023 18:00</span>
                    </div>
                    <div className={styles.div1}>
                        <b>Тема вебинара:</b>
                        <span>
              <span className={styles.span}>{` `}</span>
              <span>Создаем бота на заказ</span>
            </span>
                    </div>
                    <div className={styles.videoplayerBackground}/>
                </div>
            </div>
            <div className={styles.createquestion}>
                <div className={styles.createquestion1}>
                    <div className={styles.secondVebinarBackground}/>
                    <div className={styles.div2}>
            <span className={styles.txt}>
              <b>
                <span>{`Чтобы задать `}</span>
                <span className={styles.span2}>вопрос</span>
              </b>
              <span>, введи его в поле ниже и нажми на кнопку отправить</span>
            </span>
                    </div>
                    <div className={styles.sendquestionbutton}>
                        <div className={styles.sendQuestionButtonBackgroun}/>
                        <b className={styles.b}>ОТПРАВИТЬ</b>
                    </div>
                    <div className={styles.writequestion}>
                        <div className={styles.writeQuestionBackground}/>
                        <div className={styles.div3}>Вопрос..</div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Vebinars;
