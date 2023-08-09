import {useCallback, useEffect, useState} from "react";
import styles from "./Profile.module.css";
import {useNavigate} from "react-router-dom";
import axios from "axios";
import {API_URL} from "../constants";



const Profile = () => {
    const [user, setUser] = useState(null);
    useEffect(() => {
        axios.get(API_URL).then((response) => {
            setUser(response.data);
        });
    }, []);
    console.log(user)

    const navigate = useNavigate()
    const onBackButtonIconClick = useCallback(() => {
        navigate('/')
    }, []);


    return (

        <div className={styles.profile}>
            <div className={styles.top}/>
            <div className={styles.info}>
                <div className={styles.info1}>
                    <div className={styles.userPhoto}/>
                    <div className={styles.textinfo}>
                        <div className={styles.div}>{user.name}</div>
                        <div className={styles.bichief}>@{user.username}
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.github}>
                <div className={styles.gitmain}>
                    <div className={styles.gitmain}>
                        <div className={styles.backgroundGithub}/>
                        <b className={styles.github2}>GitHub</b>
                    </div>
                    <div className={styles.gitlink}>
                        <div className={styles.githubLink}/>
                        <div className={styles.div1}>{user.github_link}</div>
                        <div className={styles.circleAroundCopy}/>
                        <img
                            className={styles.copyDocumentSvgrepoCom1Icon}
                            alt=""
                            src="/copydocumentsvgrepocom-1.svg"
                        />
                    </div>
                </div>
            </div>
            <div className={styles.moreinfo}>
                <div className={styles.moreinfo1}>
                    <div className={styles.maininfoprofile}/>
                    <div className={styles.level}>
                        <div className={styles.div2}>Уровень:</div>
                        <b className={styles.b}>{user.rating}</b>
                        <b className={styles.b1}>5/50</b>
                    </div>
                    <div className={styles.date}>
                        <div className={styles.div2}>Дата регистрации:</div>
                        <b className={styles.b2}>{user.connect_date}</b>
                    </div>
                </div>
            </div>
            <div className={styles.levelup}>
                <div className={styles.levelup1}>
                    <div className={styles.bigBackgroundProfile}/>
                    <b className={styles.b3}>
            <span className={styles.txt}>
              <span>{`Как повысить `}</span>
              <span className={styles.span}>уровень</span>
              <span>?</span>
            </span>
                    </b>
                    <div className={styles.div4}>
                        Все просто. По мере прохождения курса будут начисляться специальные
                        баллы, которые позволят подняться вверх по ТОПу. Не забывай про чат
                        - общаясь, помогая другим участникам ты так же получаешь очки.
                    </div>
                    <div className={styles.leveltable}>
                        <div className={styles.lines}>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                            <div className={styles.linesChild}/>
                        </div>
                        <div className={styles.secondLvl}>
                            <div className={styles.div5}>50 баллов</div>
                            <div className={styles.it}>Вошел в IT</div>
                        </div>
                        <div className={styles.thirdLvl}>
                            <div className={styles.div6}>100 баллов</div>
                            <div className={styles.div7}>Прошаренный</div>
                        </div>
                        <div className={styles.fourthLvl}>
                            <div className={styles.div8}>200 баллов</div>
                            <div className={styles.div9}>Прогер</div>
                        </div>
                        <div className={styles.fiveLvl}>
                            <div className={styles.div8}>300 баллов</div>
                            <div className={styles.it100lvl}>ITшник 100LVL</div>
                        </div>
                        <div className={styles.sixLvl}>
                            <div className={styles.div11}>400 баллов</div>
                            <div className={styles.div12}>Модер</div>
                        </div>
                        <div className={styles.sixLvl1}>
                            <div className={styles.div11}>600 баллов</div>
                            <div className={styles.div14}>Правая рука</div>
                        </div>
                        <div className={styles.firrstLvl}>
                            <div className={styles.div15}>0 баллов</div>
                            <div className={styles.div16}>Новичок</div>
                        </div>
                        <div className={styles.buttonmore}>
                            <div className={styles.buttonmoreChild}/>
                            <div className={styles.div17}>Подробнее</div>
                        </div>
                        <div className={styles.div18}>Баллы</div>
                        <div className={styles.div19}>Название</div>
                    </div>
                </div>
            </div>
            <img
                className={styles.backButtonIcon}
                alt=""
                src="/back-button.svg"
                onClick={onBackButtonIconClick}
            />
        </div>
    );

};
export default Profile;
