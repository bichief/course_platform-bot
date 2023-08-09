import {useCallback} from "react";
import styles from "./Refferal.module.css";
import {useNavigate} from "react-router-dom";

const Refferal = () => {
    const navigate = useNavigate()
    const onBackButtonIconClick = useCallback(() => {
        navigate('/')
    }, []);

    return (
        <div className={styles.refferal}>
            <div className={styles.top}/>
            <div className={styles.mainref}>
                <div className={styles.mainref1}>
                    <div className={styles.amountRefBackground}/>
                    <b className={styles.b}>Ты пригласил:</b>
                    <div className={styles.div}>0</div>
                    <div className={styles.div1}>друзей</div>
                </div>
            </div>
            <div className={styles.balanceref}>
                <div className={styles.balanceref1}>
                    <div className={styles.balanceRefBackgroud}/>
                    <b className={styles.b1}>Твой бонусный баланс:</b>
                    <div className={styles.moneyref}>
                        <div className={styles.div2}>0</div>
                        <div className={styles.div3}>рублей</div>
                    </div>
                </div>
            </div>
            <div className={styles.inforef}>
                <div className={styles.inforef1}>
                    <div className={styles.backgroundInforef}/>
                    <div className={styles.inforeftext}>
                        <b className={styles.b2}>
              <span className={styles.txt}>
                <span>{`Как работает `}</span>
                <span className={styles.span}>система</span>
                <span>?</span>
              </span>
                        </b>
                        <div className={styles.div4}>
              <span className={styles.txt}>
                <p className={styles.p}>
                  Система приведи друга работает по следующему принципу:
                </p>
                <p className={styles.p1}>
                  Ты отправляешь ссылку, прикрепленную ниже своему другу и если
                  он приобретает курс, твой бонусный баланс пополняется на 500
                  рублей.
                </p>
              </span>
                        </div>
                    </div>
                    <div className={styles.reflink}>
                        <div className={styles.copylink}>
                            <div className={styles.referralLinkBack}/>
                            <div className={styles.div5}>реферральная ссылка</div>
                            <div className={styles.circleAroundCopy}/>
                            <img
                                className={styles.copyDocumentSvgrepoCom1Icon}
                                alt=""
                                src="/copydocumentsvgrepocom-1.svg"
                            />
                        </div>
                        <div className={styles.div6}>
              <span className={styles.txt}>
                <span>{`Твоя реферальная `}</span>
                <span className={styles.span}>ссылка</span>
                <span>:</span>
              </span>
                        </div>
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

export default Refferal;
