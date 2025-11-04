import { useState } from "react";
import "../css/SportCard.css";
import CardOverlay from "./CardOverlay";

function SportCard(props: SportCardProps) {
    const [activeOverlay, setActiveOverlay] = useState(false);

    async function handleClick() {
        setActiveOverlay(true)
    }

    return (
        <div className="card-container" onClick={handleClick}>
            <div className="card-header">
                <span className={`card-sport ${props.sport}`}>{props.sport}</span>
                <span className="card-status">
                    {props.live ? "LIVE" : props.score1 ? "FINISHED" : "UPCOMING"}
                </span>
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
                <div title="Match Location" className="card-location">{props.location_name}</div>
            </div>
            {
                activeOverlay && <CardOverlay
                    setIsOverlay={setActiveOverlay}
                    isOverlay={activeOverlay}
                    match_id={props.match_id}
                />
            }
        </div>
    );
}

export default SportCard;
