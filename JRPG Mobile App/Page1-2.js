import * as React from 'react';
import { Text, View, Pressable ,StyleSheet, Dimensions, Platform, Image, ImageBackground, Button } from 'react-native';
import { Audio } from 'expo-av';



function PlayBackgroundMusicPage1() {
  (async () => {
    try {
      await Audio.setIsEnabledAsync(true);
      const sound = new Audio.Sound();
      await sound.loadAsync(require('./Bravely.mp3'));
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

export default class Page1 extends React.Component {
  render() {
    PlayBackgroundMusicPage1();
    return (
      <View style={styles.page}>
        <Text style={styles.pageTitle}>Tiz Arrior</Text>
        <Pressable onPress={() => this.props.goToPage('Home')}>
          <Text> Rean Shwarzer</Text>
        </Pressable>
        <Pressable onPress={() => this.props.goToPage('Page2')}>
          <Text> Ren Amamiya </Text>
        </Pressable>

<Image source={require('./Tiz.jpg')} style={{height:'50%', width:'80%', alignSelf:'center'}} ></Image>
        <Text style={styles.page}>

        Tiz Arrior is the son of a farmer from an unnamed village. He was happy until his village was destroyed due to a calamity.
        {"\n"}{"\n"}
        He would soon find out that a military group was in charge of the village's destruction.
        {"\n"}{"\n"}
        By using the power of the asterisk he saved the world from the military's tyranny.
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
    backgroundColor: 'lightblue',
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

