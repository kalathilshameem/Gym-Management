WORKOUT_PLANS = {
    'weight_loss': {
        'title': 'Fat Burn Program',
        'duration': '8 Weeks',
        'exercises': [
            'HIIT Training (30 mins)',
            'Boxing Circuit',
            'Cycling Intervals',
            'Plyometric Drills'
        ],
        'nutrition': 'High protein, low carb diet with a calorie deficit'
    },
    'muscle_gain': {
        'title': 'Muscle Builder Program',
        'duration': '12 Weeks',
        'exercises': [
            'Compound Lifts Pyramid Sets',
            'Isolation Exercises',
            'Drop Sets Training',
            'Negative Reps Training'
        ],
        'nutrition': 'Calorie surplus with 2g protein/kg body weight'
    },
    'weight_gain': {
        'title': 'Healthy Bulk Program',
        'duration': '10 Weeks',
        'exercises': [
            'Strength Training (4x a week)',
            'Progressive Overload Training',
            'Heavy Lifting with Controlled Reps',
            'Core Strength Workouts'
        ],
        'nutrition': 'High-calorie intake with nutrient-dense foods (healthy fats, lean protein, and complex carbs)'
    },
    'endurance': {
        'title': 'Stamina & Conditioning Program',
        'duration': '6 Weeks',
        'exercises': [
            'Long-Distance Running (5km+)',
            'Cycling Endurance Sessions',
            'Jump Rope Cardio Drills',
            'High-Rep Bodyweight Workouts'
        ],
        'nutrition': 'Balanced diet rich in complex carbs and lean protein for sustained energy'
    },
    'flexibility': {
        'title': 'Agility & Recovery Program',
        'duration': '4 Weeks',
        'exercises': [
            'Dynamic Stretching Routine',
            'Yoga Flow Sessions',
            'Foam Rolling & Recovery',
            'Balance & Coordination Drills'
        ],
        'nutrition': 'Anti-inflammatory foods like turmeric, ginger, omega-3-rich foods, and hydration focus'
    }
}


def generate_workout(goal):
    return WORKOUT_PLANS.get(goal.lower(), WORKOUT_PLANS['weight_loss'])
