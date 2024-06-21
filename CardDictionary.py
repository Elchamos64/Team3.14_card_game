from Card import Card

cards = {
        "Sword Slash": Card("Sword Slash", "Images/Card/SwordSlash.png", "Deal 2-3 Damage",  ["attack", 2,3,1]),
        "Heal Potion": Card("Heal Potion", "Images/Card/HealingPotion.png", "Heal 0-5 Health", ["heal", 0,5,1]),
        "Shield Block": Card("Shield Block", "Images/Card/Block.png", "Block 5-9 Damage", ["block", 5,9,1]),
        "Kick": Card("Kick", "Images/Card/Kick.png", "Deal 0-5 Damage", ["attack", 0,5,1]),
        "Hide": Card("Hide", "Images/Card/Hide.png", "Block 10 Damage", ["block", 10, 10, 2])
    }