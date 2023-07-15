import * as React from 'react';
import { Text, View, Pressable ,StyleSheet, Dimensions, Platform, Image, ImageBackground, Button } from 'react-native';
import { Audio } from 'expo-av';



function PlayBackgroundMusicPage2() {
  (async () => {
    try {
      await Audio.setIsEnabledAsync(true);
      const sound = new Audio.Sound();
      await sound.loadAsync(require('./Persona.mp3'));
      await sound.setIsLoopingAsync(true);
      // A number between 0.0 (silence) and 1.0
      await sound.setVolumeAsync(1);
      await sound.playAsync(true);
      // unload from memory
      // await sound.unloadAsync();
    } catch (error) {
      console.error(error);
    }
  })();
}




export default class Page2 extends React.Component {
  render() {
    PlayBackgroundMusicPage2();
    return (
      <View style={styles.page}>
        <Text style={styles.pageTitle}>Ren Amamiya</Text>
        <Pressable onPress={() => this.props.goToPage('Home')}>
          <Text> Rean Shwarzer</Text>
        </Pressable>
        <Pressable onPress={() => this.props.goToPage('Page1')}>
          <Text> Tiz Arrior</Text>
        </Pressable>
        <Image source={require('./Joker.jpg')} style={{height:'50%', width:'80%', alignSelf:'center'}} ></Image>
        <Text style={styles.page}>

        Ren was a normal teenager living at home until he was unjustly arrested for a crime he didn't commit.
        {"\n"}{"\n"}
        After finding a new school he awakend to the power of persona.
        {"\n"}{"\n"}
        Using this power he created the phantom thieves who had the ability to change the hearts of wicked people in society.
        </Text>
        
      </View>
    );
  }
}

const styles = StyleSheet.create({
  page: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'darkred',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  pageTitle: {
    margin: 10,
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
