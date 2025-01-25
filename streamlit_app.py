import streamlit as st

health = 100
money = 0

if 'page' not in st.session_state:
    st.session_state.page = 'start'

def change_page(new_page):
    st.session_state.page = new_page

if st.session_state.page == 'start':
    st.title('welcome to the adventure')
    st.write('you wake up in a forest. there are 2 ways in front of you. choose one.')
    left = st.button('left')
    right = st.button('right')

    if left == True:
        change_page('left')
    elif right == True:
        change_page('right')

elif st.session_state.page == 'left':
    st.title('you choose left')
    st.write('you see a tiger. choose what to do.')
    fight = st.button('fight')
    run = st.button('run')

    if fight == True:
        health -= 60
        money += 0
        st.title('VICTORY')
        st.write('you fought well. but you sacrificed some of your health. you may find some medikit and money ahead in your journey.')
        st.write('health =' ,health)
        st.write('moeny =' ,money)
        change_page('river')
    
    elif run == True: 
        st.write('you should have fought')
        change_page('start')

elif st.session_state.page == 'right':
    st.title('chest')
    st.write('you encountered a chest. choose what to do.')
    open_chest = st.button('open')
    skip_chest = st.button('skip')
    
    if open_chest == True:
        health += 0
        money += 100
        st.title('congratulations!!')
        st.write('you earned $100. this money can be used ahead in a shop to buy items.')
        st.write('health =' ,health)
        st.write('money =' ,money)
        change_page('cave')

    elif skip_chest == True:
        health += 0
        money += 0
        st.write('do not skip chests!')
        st.write('health =' ,health)
        st.write('money =' ,money)
        change_page('cave')

elif st.session_state.page == 'river':
    st.title('river')
    st.write('while walking on the river bank you see a medikit and some money. choose one.')
    medikit_pick = st.button('medikit')
    money_pick = st.button('money')

    if medikit_pick == True:
        health = 100
        money += 0
        st.write('you restored your health')
        st.write('health =' ,health)
        st.write('money =' ,money)
        change_page('crocodile_win')

    elif money_pick == True:
        health += 0
        money += 100
        st.title('congratulations!!')
        st.write('you earned $100. this money can be used ahead in a shop to buy items.')
        st.write('health =' ,health)
        st.write('money =' ,money)
        change_page('crocodile_loose')

elif st.session_state.page == 'cave':
    st.title('cave')
    st.write('there is shop, you can use it to buy items')
    buy = st.button('buy')
    skip = st.button('skip')

    if buy == True:
        change_page('shop')
        
elif st.session_state.page == 'shop':
    st.title('Shop')
    st.write('you can only buy one item')
    medikit = st.button('buy medikit $15')
    weapon = st.button('buy weapon $60')

    if medikit == True:
        money = 100-15
        health = 100
        st.write('health =' ,health)
        st.write('money =' ,money)
        st.title('congratulations!')
        st.write('the medikit will be automatically used if you loose health') 
        change_page('zombie_win')

    elif weapon == True:
        money = 100 - 65
        health = 100
        st.write('health =' ,health)
        st.write('money =' ,money)
        st.title('congratulations!')
        st.write('the weapon can now be used in fights to give more damage to the oponent which would cost you less health')
        change_page('zombie_win')

elif st.session_state.page == 'crocodile_win':
    st.title('you see a crocodile')
    fight = st.button('fight')
    run = st.button('run')

    if fight == True:
        st.title('VICTORY')
        st.write('as you move forward you now see a boat which can be used to escape.')
        escape = st.button('escape')

        if escape == True:
            change_page('ending')

    elif run == True:
        st.write('you should have fought')
        change_page('river')

elif st.session_state.page == 'crocodile_loose':
    st.title('you see a crocodile')
    fight = st.button('fight')
    run = st.button('run')

    if fight == True:
        st.title('Wasted')
        st.write('you died due to low health')
        change_page('start')

    elif run == True:
        st.write('you should have fought')
        change_page('river')

elif st.session_state.page == 'zombie_win':
    st.title('zombie fight')
    st.write('zombies are coming towards you')
    fight = st.button('fight')
    run = st.button('run')

    if fight == True:
        st.title('VICTORY')
        change_page('zombie_boss')

    elif run == True:
        st.write('you should have fought')
        change_page('zombie_win')

elif st.session_state.page == 'zombie_boss':
    st.title('Zombie boss')
    st.write('the zombie boss is waiting for you')
    fight = st.button('fight')
    run = st.button('run')

    if fight == True:
        st.title('VICTORY')
        st.write('as you move out of the cave you see a flair gun')
        flair = st.button('fire the gun')

        if flair == True:
            change_page('escape')

    elif run == True:
        st.write('you should have fought')
        change_page('zombie_boss')

elif st.session_state.page == 'escape':
    st.title('escape')
    st.write('a helicopter aproaches you')
    escape = st.button('escape')
    
    if escape == True:
        st.write('you successfully escaped the forest')
        change_page('ending')

elif st.session_state.page == 'ending':
    st.title('end')
    st.write('you finished the game!!')
    reset = st.button('reset')

    if reset == True:
        change_page('start')
