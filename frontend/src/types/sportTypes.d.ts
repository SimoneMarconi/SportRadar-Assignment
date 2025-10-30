type SportCardProps = {
  match_id: number;
  team1: string;
  team2: string;
  live: boolean;
  sport: string;
  score1?: number;
  score2?: number;
  location_name: string;
  tickets_sold: number;
  date: string;
  time: string;
  description?: string;
};

type PageFilterProps = {
  filter: CardStatus;
  setFilter: React.Dispatch;
};

type OverlayProps = {
    match_id: number
    isOverlay: boolean
    setIsOverlay: React.Dispatch<React.SetStateAction<boolean>>
}

type MatchInfo = {
    match_description: string
    team1: string
    team2: string
    team1_description: string
    team2_description: string
    coordinates: string
    tickets_sold: number
    total_seats: number
}
