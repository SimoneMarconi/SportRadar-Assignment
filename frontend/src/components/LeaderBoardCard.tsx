import "../css/LeaderBoardCard.css"

function LeaderBoardCard(props: LeaderBoardCardProps) {
    return <div className="leadercard-container">
        <span className="leaderteam-name">{props.team_name}</span>
        <span className="leaderteam-wins">{props.wins}</span>
        <span className="leaderteam-location">{props.location_name}</span>
    </div>
}

export default LeaderBoardCard
