import { CardStatus } from "../types/sportEnums";
import "../css/PageFilter.css"
import FilterButton from "./FilterButton";

function PageFilter(props: PageFilterProps) {

    const buttons = [
        {label: "Live", cardStatus: CardStatus.LIVE},
        {label: "Upcoming", cardStatus: CardStatus.UPCOMING},
        {label: "Finished", cardStatus: CardStatus.FINISHED}
    ]

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
        {buttons.map((b) => <button className={`pagefilter-button ${props.filter === b.cardStatus ? "active" : ""}`} onClick={handleClick} key={b.label}>{b.label}</button>)}
        <FilterButton />
    </div>
}

export default PageFilter
