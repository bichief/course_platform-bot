import {useCallback, useEffect} from "react";
import styles from "./MainPage.module.css";
import {useNavigate} from "react-router-dom";

const MainPage = () => {
    const navigate = useNavigate()
    const onButton4ContainerClick = useCallback(() => {
        navigate('/rate')
    }, []);

    const onButton1ContainerClick = useCallback(() => {
        navigate('/ref')
    }, []);

    const onButton2ContainerClick = useCallback(() => {
        navigate('/veb')
    }, []);

    const onButton3ContainerClick = useCallback(() => {
        navigate('/faq')
    }, []);

    const onTelegramContainerClick = useCallback(() => {
        window.open("https://t.me/botd0t");
    }, []);

    const onLevelContainerClick = useCallback(() => {
        navigate('/profile')
    }, []);



    return (
        <div className={styles.mainpage}>
            <div className={styles.top}/>
            <div className={styles.menu}>
                <div className={styles.menu1}>
                    <div className={styles.button4} onClick={onButton4ContainerClick}>
                        <div className={styles.backgroundButton4}/>
                        <img className={styles.icon} alt="" src="/logo.svg"/>
                        <b className={styles.b}>Программа курса</b>
                    </div>
                    <div className={styles.button1Parent}>
                        <div className={styles.button1} onClick={onButton1ContainerClick}>
                            <div className={styles.backgroundButton1}/>
                            <div className={styles.div}>
                <span className={styles.txt}>
                  <p className={styles.p}>Зови</p>
                  <p className={styles.p}>друзей</p>
                </span>
                            </div>
                            <div className={styles.div1}>
                <span className={styles.txt}>
                  <span>{`Дарим скидку `}</span>
                  <span className={styles.span}>500₽</span>
                  <span> за приведенного друга</span>
                </span>
                            </div>
                            <img
                                className={styles.bueArrowIcon}
                                alt=""
                                src="/bue-arrow.svg"
                            />
                        </div>
                        <div className={styles.button1} onClick={onButton2ContainerClick}>
                            <div className={styles.backgroundButton2}/>
                            <div className={styles.div2}>Вебинары</div>
                            <div className={styles.div3}>Просмотр текущего вебинара</div>
                            <img
                                className={styles.bueArrowIcon}
                                alt=""
                                src="/bue-arrow.svg"
                            />
                        </div>
                        <div className={styles.button3} onClick={onButton3ContainerClick}>
                            <div className={styles.backgroundButton1}/>
                            <div className={styles.faq}>F.A.Q.</div>
                            <div className={styles.div4}>
                <span className={styles.txt}>
                  <p className={styles.p}>Ответим на</p>
                  <p className={styles.p}>частые вопросы</p>
                </span>
                            </div>
                            <img
                                className={styles.bueArrowIcon2}
                                alt=""
                                src="/bue-arrow.svg"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.telegram}>
                <div className={styles.telegram1} onClick={onTelegramContainerClick}>
                    <div className={styles.backgroundTelegramButton}/>
                    <div className={styles.telegram2}>Telegram-канал</div>
                    <b className={styles.botd0t}>@botd0t</b>
                </div>
            </div>
            <div className={styles.level}>
                <div className={styles.level1} onClick={onLevelContainerClick}>
                    <div className={styles.avatar}/>
                    <div className={styles.levelstatus}>
                        <div className={styles.statusBackground}/>
                        <div className={styles.div5}>Новичок</div>
                    </div>
                    <b className={styles.b1}>Александр</b>
                    <img
                        className={styles.blackArrowIcon}
                        alt=""
                        src="/black-arrow.svg"
                    />
                </div>
            </div>
            <div className={styles.lineUnder}/>
        </div>
    );
};

export default MainPage;
