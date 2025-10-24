#Problem 1 
# class SongNode:
#     def __init__(self, song, next=None):
#         self.song = song
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()

# node_bad_romance = SongNode("Bad Romance")
# node_party_rock = SongNode("Party Rock Anthem", node_bad_romance)
# node_uptown_funk = SongNode("Uptown Funk", node_party_rock)
        
# print_linked_list(node_uptown_funk)

# Problem 2
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# def get_artist_frequency(playlist):
#     temp = {}
     
#     current = playlist
#     while current:
#         artist = current.artist
#         if artist in temp:
#             temp[artist] += 1
#         else:
#             temp[artist] = 1
#         current = current.next
#     return temp

# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

# Problem 3
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

# Problem 4 
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True # cycle in it
    return False # no cycle

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))


# Problem 5
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head
    
    count = 1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # found the cycle
            # counting the length
            fast = fast.next
            while slow != fast:
                count += 1
                fast = fast.next
            return count
    return 0

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))

# Problem 6
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0
    before = song_audio
    this = song_audio.next
    after = this.next
    count = 0
    while after:
        if (after.value > this.value and before.value > this.value) or (after.value < this.value and before.value < this.value) :
            count += 1
        before = this
        this = after
        after = after.next
    return count 
 
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))



    