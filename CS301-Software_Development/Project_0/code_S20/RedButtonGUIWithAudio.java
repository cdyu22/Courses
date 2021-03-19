package edu.wm.cs.cs301.redbutton;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.LineEvent;
import javax.sound.sampled.LineListener;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.JButton;
import javax.swing.JFrame;
/**
* This class contains a trivial GUI that extends from the classic Hello World example.
* Its main purpose is to demo various concepts of Java. 
* It exceeds the basic version by showing how to play audio in response to 
* a button click.
* 
* @author Kemper
*
*/
public class RedButtonGUIWithAudio extends RedButtonGUI implements LineListener {
	/**
	 * Reference to audio clip that is played in response to a button click.
	 * Refers to file win.wav
	 */
	Clip audio; 

	/**
	 * Indicates whether the playback is complete or not.
	 */
	boolean playCompleted;
	
	/**
	 * Constructor initializes audio and sets up graphics.
	 */
	public RedButtonGUIWithAudio() {
		// load audio file
		audio = loadAudioClip();		
		// add another button listener to the button
		// inherited from super class
		JButton b = this.getButton();
		b.addActionListener(new ActionListener(){  
			public void actionPerformed(ActionEvent e){  
				System.out.println("Button clicked");
				try {
					playAudio(audio);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}  
		});
	}

	/**
	 * Loads the audio clip win.wav from the resource folder.
	 * file is in "res/audio/win.wav", implementation should work 
	 * on *nix and windows platforms
	 * @return clip with audio, can be null
	 */
	private Clip loadAudioClip() {
		try {
			/*
			 * Constant, hard-coded file name for the audio file such as res/audio/win.wav
			 * are a bad programming practice because path separators are system dependent
			 * https://docs.oracle.com/javase/7/docs/api/java/io/File.html
			 * https://www.sghill.net/how-do-i-make-cross-platform-file-paths-in-java.html
			 */
			// just for demonstration purposes, home and currentDir are unused
			String home = System.getProperty("user.home"); // home directory
			Path currentDir = Paths.get(".");              // current directory
			// the real code:
			// create a relative path with correct file path separator on *nix and Windows
			Path audioFilePath = Paths.get("res", "audio", "win.wav");
			// check if successful
			if (!Files.exists(audioFilePath)) {
				System.out.println("The specified audio file does not exist:" + audioFilePath);
				throw new IOException();
			}
			// MEMO: there should be a simpler way to get the AudioInputStream from the audioFilePath
			AudioInputStream audioStream =  
	                AudioSystem.getAudioInputStream(new File(audioFilePath.toAbsolutePath().toString()));   
			AudioFormat format = audioStream.getFormat();
			DataLine.Info info = new DataLine.Info(Clip.class, format);
			Clip audioClip = (Clip) AudioSystem.getLine(info);
			audioClip.addLineListener(this);
			audioClip.open(audioStream);
			return audioClip;
		}
		catch (UnsupportedAudioFileException ex) {
			System.out.println("The specified audio file is not supported.");
			ex.printStackTrace();
		} catch (LineUnavailableException ex) {
			System.out.println("Audio line for playing back is unavailable.");
			ex.printStackTrace();
		} catch (IOException ex) {
			System.out.println("Error playing the audio file.");
			ex.printStackTrace();
		}
		return null;
	}

	/**
	 * Play the given audio clip.
	 * Can be also used to replay a clip as we set the starting frame to zero.
	 * The method leaves the clip open for later reuse.
	 * @param audioClip to play.
	 */
	void playAudio(Clip audioClip) throws InterruptedException{
		playCompleted = false;
		audioClip.setFramePosition(0);
		audioClip.start();
		// Note: audio plays asynchronously and code 
		// on this thread continues execution, so
		// we need to wait till the listener tells us 
		// that the audio playback is complete
		// This loop is a form of active waiting or polling,
		// it is not(!) the best way to handle this situation.
		// Consider a wait/notify solution for improving this code.
		while (!playCompleted) {
			Thread.sleep(1000);
		}
	}

	/**
	 * Listens to the START and STOP events of the audio line.
	 * @param event listening to, only start and stop matter
	 */
	@Override
	public void update(LineEvent event) {
		LineEvent.Type type = event.getType();

		if (type == LineEvent.Type.START) {
			System.out.println("Playback started.");

		} else if (type == LineEvent.Type.STOP) {
			playCompleted = true;
			System.out.println("Playback completed.");
		}

	}
	/**
	 * Main method runs red button gui such that it plays audio.
	 * Parameters are not used.
	 * @param args are ignored
	 */
	public static void main(String[] args) {
		System.out.println("This is a different main method than in the super class!!!") ;
		
		
		if (0 < args.length) {
			System.out.println("Warning: any parameters provided on command line are ignored!");
		}
		
		final JFrame window = new JFrame("The Button Frame");
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		RedButtonGUI gui = new RedButtonGUIWithAudio() ;
		gui.setColor("red") ; // adjustment: always use red as color
		window.setContentPane(gui);
		window.pack(); 
		boolean b = true ; 
		window.setVisible(b);  
		window.setResizable(true);
	}
}
