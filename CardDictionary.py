from Card import Card

cards = {
        "Sword Slash": Card("Sword Slash", "Images/Card/SwordSlash.png", "Deal 7-10 Damage",  ["attack", 7,10,1]),
        "Heal Potion": Card("Heal Potion", "Images/Card/HealingPotion.png", "Heal 0-5 Health", ["heal", 0,5,1]),
        "Shield Block": Card("Shield Block", "Images/Card/Block.png", "Block 8-9 Damage", ["block", 8,9,1]),
        "Kick": Card("Kick", "Images/Card/Kick.png", "Deal 0-16 Damage", ["attack", 2,14,1]),
        "Hide": Card("Hide", "Images/Card/Hide.png", "Block 10 Damage", ["block", 12, 12, 2]),
        "Investigate": Card("Investigate", "Images/Card/Investigate.png", "Draw 2-3 Cards", ["draw", 2, 3, 1]),
        "Eureka!": Card("Eureka!", "Images/Card/Eureka.png", "Draw 0-2 Cards", ["draw", 0, 2, 0]),
        "Near Miss": Card("Near Miss", "Images/Card/NearMiss.png", "Heal 0-20 Health", ["heal", 0,20,3]),
        "Shruiken": Card("Shruiken", "Images/Card/NinjaStar.png", "Deal 4 Damage", ["attack", 4,4,0]),
        "Fireball": Card("Fireball", "Images/Card/Fireball.png", "Deal 23-33 Damage", ["attack", 23,33,3]),
    }