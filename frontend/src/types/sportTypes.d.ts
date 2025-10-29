type SportCardProps = {
    team1: string
    team2: string
    isLive: boolean
    sport: string
    score1?: number
    score2?: number
    location_name: string
    tickets_sold: number
    date: string
    time: string
    description?: string
}

type PageFilterProps = {
    filter: CardStatus
    setFilter: React.Dispatch
}
