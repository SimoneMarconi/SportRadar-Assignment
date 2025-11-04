import "../css/LeaderBoardCard.css"

function LeaderBoardCard(props: LeaderBoardCardProps) {
    return <div className="leadercard-container">
        <span title="Team name" className="leaderteam-name">{props.team_name}</span>
        <span title="Total wins" className="leaderteam-wins">{props.wins}</span>
        <span title="Club Headquarters" className="leaderteam-location">{props.location_name}</span>
    </div>
}

export default LeaderBoardCard
