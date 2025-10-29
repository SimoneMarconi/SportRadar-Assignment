import "../css/SportCard.css"

function SportCard({props}: {props: SportCardProps}) {
    return <div className="card-container">
        <div className="card-header">
            <span className="card-sport">{props.sport}</span>
            <span className="card-status">{props.isLive ? "LIVE" : props.score1 ? "FINISHED" : "UPCOMING"}</span>
        </div>
        <div className="card-main">
            <div className="team-block">
                <div className="team-name">{props.team1}</div>
                <div className="team-score">{props.score1}</div>
            </div>
            <div className="team-versus">VS</div>
            <div className="team-block">
                <div className="team-name">{props.team2}</div>
                <div className="team-score">{props.score2}</div>
            </div>
        </div>
        <div className="card-bottom">
            <div className="card-time">
                {props.date} {props.time}
            </div>
            <div className="card-location">{props.location_name}</div>
        </div>
    </div>
}

export default SportCard
