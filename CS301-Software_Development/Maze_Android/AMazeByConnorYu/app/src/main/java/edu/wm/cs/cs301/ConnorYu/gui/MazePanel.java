package edu.wm.cs.cs301.ConnorYu.gui;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Paint;
import android.graphics.Paint.Style;
import android.graphics.Path;
import android.graphics.RectF;
import android.util.AttributeSet;
import android.view.View;
import android.graphics.Canvas;
import android.util.Log;
import android.graphics.Color;

//Very used source: https://code.tutsplus.com/tutorials/android-sdk-creating-custom-views--mobile-14548
public class MazePanel extends View implements P5Panel {
	Paint paint;

	//https://stackoverflow.com/questions/5663671/
	Bitmap.Config conf = Bitmap.Config.ARGB_8888;
	Bitmap bmp = Bitmap.createBitmap(1440,2308,conf);
	Canvas panel = new Canvas(bmp);

	public MazePanel(Context context, AttributeSet attrs){
		super(context,attrs);

		paint = new Paint();
		paint.setColor(getColorEncoding(255,0,0));

		Log.v("MazePanel","Called MazePanel");
	}

	//https://stackoverflow.com/questions/5729377/
	@Override
	public void clear() {
		panel.drawColor(Color.WHITE);
	}

	@Override
	public void commit() {
		invalidate();
	}

	@Override
	public boolean isOperational() {
		return true;
	}

	@Override
	public void onDraw(Canvas canvas){
		Bitmap scaledBitmap = Bitmap.createScaledBitmap(bmp,4000,6000,true);
		canvas.drawBitmap(scaledBitmap,0,0,paint);
		clear();
	}

	//*******************************Handling Drawing Methods*************************************
	//Reference: https://stackoverflow.com/questions/18022364/
	public static int getColorEncoding(int red, int green, int blue){
		int RGB = android.graphics.Color.argb(255,red,green,blue);
		return RGB;
	}

	@Override
	public void setColor(int rgb) { paint.setColor(rgb); }

	@Override
	public int getColor() {
		int RGB = paint.getColor();
		return RGB;
	}

	@Override
	public void addFilledRectangle(int x, int y, int width, int height) {
		paint.setStyle(Style.FILL);
		panel.drawRect(x,x,y,x+height,paint);
	}

	//Polygon reference: https://stackoverflow.com/questions/2047573/how-to-draw-filled-polygon
	@Override
	public void addFilledPolygon(int[] xPoints, int[] yPoints, int nPoints) {
		paint.setStyle(Style.FILL);

		Path path = new Path();
		path.reset();
		path.moveTo(xPoints[0],yPoints[0]);

		for(int i = 1; i < nPoints; i++){
			path.lineTo(xPoints[i],yPoints[i]);
		}

		path.close();
		panel.drawPath(path,paint);
	}

	@Override
	public void addPolygon(int[] xPoints, int[] yPoints, int nPoints) {
		paint.setStyle(Style.STROKE);

		Path path = new Path();
		path.reset();
		path.moveTo(xPoints[0],yPoints[0]);

		for(int i = 1; i < nPoints; i++){
			path.lineTo(xPoints[i],yPoints[i]);
		}

		path.close();
		panel.drawPath(path,paint);
	}

	@Override
	public void addLine(int startX, int startY, int endX, int endY) {
		panel.drawLine(startX,startY,endX,endY,paint);
	}

	//https://stackoverflow.com/questions/5012685/
	@Override
	public void addFilledOval(int x, int y, int width, int height) {
		paint.setStyle(Style.FILL);

		RectF rect = new RectF(x,y,x+width,y+height);
		panel.drawOval(rect,paint);
	}

	@Override
	public void addArc(int x, int y, int width, int height, int startAngle, int arcAngle) {
		panel.drawArc(x,y,x+width,y+height,startAngle,arcAngle,true,paint);
	}

	@Override
	public void addMarker(float x, float y, String str) {
		paint.setTextAlign(Paint.Align.CENTER);
		paint.setTextSize(14);
		panel.drawText(str, x, y, paint);
	}

	//https://medium.com/@quiro91/custom-view-mastering-onmeasure-a0a0bb11784d
	//*******************************Handling Drawing Methods*************************************
	@Override
	protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
		Log.v("Chart onMeasure w", MeasureSpec.toString(widthMeasureSpec));
		Log.v("Chart onMeasure h", MeasureSpec.toString(heightMeasureSpec));

		int desiredWidth = getSuggestedMinimumWidth() + getPaddingLeft() + getPaddingRight();
		int desiredHeight = getSuggestedMinimumHeight() + getPaddingTop() + getPaddingBottom();

		setMeasuredDimension(measureDimension(desiredWidth, widthMeasureSpec),
				measureDimension(desiredHeight, heightMeasureSpec));
	}

	private int measureDimension(int desiredSize, int measureSpec) {
		int result;
		int specMode = MeasureSpec.getMode(measureSpec);
		int specSize = MeasureSpec.getSize(measureSpec);

		if (specMode == MeasureSpec.EXACTLY) {
			result = specSize;
		} else {
			result = desiredSize;
			if (specMode == MeasureSpec.AT_MOST) {
				result = Math.min(result, specSize);
			}
		}
		return result;
	}
}
