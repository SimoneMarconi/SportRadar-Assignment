import { CardStatus } from "../types/sportEnums";
import "../css/PageFilter.css"

function PageFilter(props: PageFilterProps) {

    function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
        const value = event.currentTarget.textContent?.toLowerCase();
        if (value === "live") {
            props.setFilter(CardStatus.LIVE);
        } else if (value === "upcoming") {
            props.setFilter(CardStatus.UPCOMING);
        } else if (value === "finished") {
            props.setFilter(CardStatus.FINISHED)
        }
    }

    return <div className="pagefilter-container">
        <button className={`pagefilter-button ${props.filter === CardStatus.LIVE ? "active" : ""}`} onClick={handleClick}>Live</button>
        <button className={`pagefilter-button ${props.filter === CardStatus.UPCOMING? "active" : ""}`} onClick={handleClick}>Upcoming</button>
        <button className={`pagefilter-button ${props.filter === CardStatus.FINISHED? "active" : ""}`} onClick={handleClick}>Finished</button>
    </div>
}

export default PageFilter
