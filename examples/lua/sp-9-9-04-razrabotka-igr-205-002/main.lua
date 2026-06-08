--!strict
export type GunSettings = {
    fireMode: "SEMI" | "AUTO",
    damage: number,
    headshotMultiplier: number,
    rateOfFire: number,
    range: number,
}

return {
    fireMode = "SEMI",
    damage = 22,
    headshotMultiplier = 2,
    rateOfFire = 450,
    range = 500,
} :: GunSettings
