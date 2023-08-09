import { useCallback } from "react";
import styles from "./FAQ.module.css";
import {useNavigate} from "react-router-dom";
const FAQ = () => {
        const navigate = useNavigate()
  const onBackButtonIconClick = useCallback(() => {
    navigate('/')
  }, []);

  return (
    <div className={styles.faq}>
      <div className={styles.top} />
      <img
        className={styles.backButtonIcon}
        alt=""
        src="/back-button.svg"
        onClick={onBackButtonIconClick}
      />
      <div className={styles.faqinfo}>
        <div className={styles.faqinfo1}>
          <div className={styles.backgroundFaqInfo} />
          <b className={styles.b}>
            <span>{`Есть `}</span>
            <span className={styles.span}>вопросы</span>
            <span>?</span>
          </b>
          <div className={styles.div}>
            Опиши свою проблему нашей поддержке и мы обязательно тебе поможем!
          </div>
          <div className={styles.supbutton}>
            <div className={styles.backgroundSupButton} />
            <b className={styles.b1}>СВЯЗАТЬСЯ</b>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FAQ;
