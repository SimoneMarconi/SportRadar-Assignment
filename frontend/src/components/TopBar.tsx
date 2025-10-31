import "../css/TopBar.css"
import { PageState } from "../types/sportEnums"

function TopBar(props: TopBarProps) {

    function handleClick(event: React.MouseEvent) {
        const value = event.currentTarget.textContent?.toLowerCase();
        if (props.page === PageState.MATCHES && value === "leaderboards") {
            props.setPage(PageState.LEADERBOARD)
        } else if (props.page === PageState. LEADERBOARD && value === "matches"){
            props.setPage(PageState.MATCHES)
        }
    }

    return <div className="bar-container">
        <button className="bar-button" onClick={handleClick}>Matches</button>
        <button className="bar-button" onClick={handleClick}>Leaderboards</button>
    </div>
}

export default TopBar
