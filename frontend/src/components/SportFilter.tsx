import { SportType } from "../types/sportEnums";

import "../css/SportFilter.css"

function SportFilter({sportFilter, setSportFilter}: SportFilterProps) {

    const sportButtons = [
        {label: "Football", type: SportType.FOOTBALL},
        {label: "BasketBall", type: SportType.BASKETBALL},
        {label: "Baseball", type: SportType.BASEBALL},
    ]

    function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
        const value = event.currentTarget.textContent?.toLowerCase();
        if (value === "football") {
            setSportFilter(SportType.FOOTBALL)
        } else if (value === "basketball") {
            setSportFilter(SportType.BASKETBALL)
        } else if (value === "baseball") {
            setSportFilter(SportType.BASEBALL)
        }
    }

    return <div className="sportfilter-container">
        {sportButtons.map(sport => <button className={`sportfilter-button ${sportFilter === sport.type ? "active" : ""}`} onClick={handleClick} key={sport.label}>{sport.label}</button>)}
    </div>
}

export default SportFilter
