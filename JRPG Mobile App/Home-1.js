import * as React from 'react';
import { Text, View, Pressable ,StyleSheet, Dimensions, Platform, Image, ImageBackground, Button } from 'react-native';
import { Audio } from 'expo-av';



function PlayBackgroundMusicPageHome() {
  (async () => {
    try {
      await Audio.setIsEnabledAsync(true);
      const sound = new Audio.Sound();
      await sound.loadAsync(require('./Trails.mp3'));
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




export default class Home extends React.Component {
  render() {
    PlayBackgroundMusicPageHome();
    return (
      <View style={styles.page}>
        <Text style={styles.pageTitle}> Rean Shwarzer</Text>
        <Pressable onPress={() => this.props.goToPage('Page1')}>
          <Text> Tiz Arrior </Text>
        </Pressable>
        <Pressable onPress={() => this.props.goToPage('Page2')}>
          <Text> Ren Amamiya </Text>
        </Pressable>
<Image source={require('./Rean.png')} style={{height:'40%', width:'80%', alignSelf:'center'}} ></Image>
        <Text style={styles.page}>

        Rean Shwarzer is a member of the Thors Military Academy Class 7.
        {"\n"}{"\n"}
        He attended as a student there for a time before the assasination of the leader of Erebonia.
        {"\n"}{"\n"}
        During the war that ensued after he and his classmates needed to bring the world back to its peaceful era.
        {"\n"}{"\n"}
        Rean soon awakend as the Ashen Awakener and was able to use the power of the divine knight Valimar.
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
    backgroundColor: 'tan',
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
