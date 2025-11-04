import { useState } from "react";
import "../css/TopBar.css"
import { PageState } from "../types/sportEnums"
import AddEventOverlay from "./AddEventOverlay";

function TopBar(props: TopBarProps) {

    const [addEventActive, setAddEventActive] = useState(false)

    function handleClick(event: React.MouseEvent) {
        const value = event.currentTarget.textContent?.toLowerCase();
        if (props.page === PageState.MATCHES && value === "leaderboards") {
            props.setPage(PageState.LEADERBOARD)
        } else if (props.page === PageState.LEADERBOARD && value === "matches") {
            props.setPage(PageState.MATCHES)
        }
    }

    function addEventClick() {
        setAddEventActive(true)
    }

    return <div className="bar-container">
        <button className="addevent-button" onClick={addEventClick}>+</button>
        {addEventActive && <AddEventOverlay isOpen={addEventActive} setIsOpen={setAddEventActive} />}
        <button className="bar-button" onClick={handleClick}>Matches</button>
        <button className="bar-button" onClick={handleClick}>Leaderboards</button>
    </div>
}

export default TopBar
